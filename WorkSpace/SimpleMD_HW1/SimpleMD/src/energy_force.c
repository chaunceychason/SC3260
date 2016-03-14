#include "energy_force.h"
#include "params.h"
#include "atoms.h"
#include "timer.h"
#include <omp.h>

//************************************************************************
// compute_long_range_correction() function
//   - Calculates long range correction due to finite interaction cutoff.
//   - Arguments:
//       - len_jo: struct containing leonard jones interaction parameters.
//       - m_pars: struct containing misc. parameters.
//       - energy_long: long-range correction to energy.
//       - force_long: long-range correction to force.
//************************************************************************
void compute_long_range_correction(const lj_params * len_jo, const misc_params * m_pars,
                                   float * energy_long, float * force_long )
{

   float ulongpre = m_pars->float_N * 8.0 * len_jo->eps * 
                    m_pars->pi * m_pars->density;
   *energy_long = ulongpre * ( len_jo->sig12 / ( 9.0 * len_jo->rcut9 ) - 
                               len_jo->sig6 / ( 6.0 * len_jo->rcut3 ) );

   float vlongpre = 96.0 * len_jo->eps * m_pars->pi * m_pars->density;
   *force_long = -1.0 * vlongpre * ( len_jo->sig12 / ( 9.0 * len_jo->rcut9 ) - 
                                     len_jo->sig6 / ( 6.0 * len_jo->rcut3 ) ); 

}

//************************************************************************
// compute_energy_and_force() function
//   - Calculates energy and force acting on each atom.
//   - Arguments:
//       - myatoms: struct containing all atomic information.
//       - len_jo: struct containing lennard jones interaction parameters.
//       - m_pars: struct containing misc. parameters.
//************************************************************************
void compute_energy_and_force( Atoms * myatoms, const lj_params * len_jo, 
                               const misc_params * m_pars )
{

   timeit(1,0);
   int atomi, atomj, i;
   #pragma simd
   for (atomi=0; atomi < myatoms->N; atomi++)
   {
      myatoms->fx[atomi] = 0.0;
      myatoms->fy[atomi] = 0.0;
      myatoms->fz[atomi] = 0.0;
   }

   myatoms->pot_energy = 0.0;
   myatoms->virial = 0.0;
   
   //float sum_pot_total = myatoms->pot_energy;
   //float sum_vir_total = myatoms->virial;
   float sum_pot_total = 0;
   float sum_vir_total = 0;

   /*
   float sum_fx_total = 0;
   float sum_fy_total = 0;
   float sum_fz_total = 0;
   */

   for (atomi=0; atomi < myatoms->N; atomi++)
   {

      float sum_local_pot[myatoms->N]; //need to initialize all elements to zero
      float sum_local_vir[myatoms->N]; 
      float sum_local_fx[myatoms->N];
      float sum_local_fy[myatoms->N];
      float sum_local_fz[myatoms->N];
      

      float sum_loco_pot_total = 0;
      float sum_loco_vir_total = 0;
      float sum_loco_fx_total = 0;
      float sum_loco_fy_total = 0;
      float sum_loco_fz_total = 0;
      

      //old: non-vectorized
      //for (atomj=atomi+1 ; atomj < myatoms->N; atomj++)
      #pragma simd
      for (atomj=0 ; atomj < myatoms->N; atomj++)
      {         
         memset(sum_local_pot, 0, myatoms->N * sizeof(sum_local_pot[0]) );
         memset(sum_local_vir, 0, myatoms->N * sizeof(sum_local_vir[0]) );

         memset(sum_local_fx, 0, myatoms->N * sizeof(sum_local_fx[0]) );
         memset(sum_local_fy, 0, myatoms->N * sizeof(sum_local_fy[0]) );
         memset(sum_local_fz, 0, myatoms->N * sizeof(sum_local_fz[0]) );

         if (atomj != atomi )
         {
            
   
            float xxi = myatoms->xx[atomi] - myatoms->xx[atomj];
            xxi = minimum_image( xxi, m_pars->side, m_pars->sideh );
            float yyi = myatoms->yy[atomi] - myatoms->yy[atomj];
            yyi = minimum_image( yyi, m_pars->side, m_pars->sideh );
            float zzi = myatoms->zz[atomi] - myatoms->zz[atomj];
            zzi = minimum_image( zzi, m_pars->side, m_pars->sideh );

            float dis2 = xxi*xxi + yyi*yyi + zzi*zzi;
            if ( dis2 <= len_jo->rcut2 )
            {
               float dis2i = 1.0 / dis2;
               float dis6i = dis2i * dis2i * dis2i;
               float dis12i = dis6i * dis6i;
               //old: non-vectorized
               //myatoms->pot_energy += len_jo->sig12 * dis12i - 
               //                       len_jo->sig6 * dis6i;
               //-----------------------------------------------
               float loco_pot_energy = 0; //local variable 
               loco_pot_energy = len_jo->sig12 * dis12i - 
                                      len_jo->sig6 * dis6i;
               sum_local_pot[atomj] = loco_pot_energy;
               //-----------------------------------------------
               
               float fterm = dis2i * ( 2.0 * len_jo->sig12 * dis12i -
                                             len_jo->sig6 * dis6i );

                             
               //myatoms->virial -= fterm * dis2;
               float loco_vir_value  = 0;    //local variable 
               loco_vir_value -= fterm * dis2;
               sum_local_vir[atomj] = loco_vir_value;

               /*
               //old: non-vectorized since atomi is not in inner loop.
               myatoms->fx[atomi] += fterm * xxi;
               myatoms->fy[atomi] += fterm * yyi;
               myatoms->fz[atomi] += fterm * zzi;
               */
               
               float loco_fx_value = 0;
               float loco_fy_value = 0;
               float loco_fz_value = 0;
               loco_fx_value += fterm * xxi;
               loco_fy_value += fterm * yyi;
               loco_fz_value += fterm * zzi;    
               sum_local_fx[atomj] = loco_fx_value;
               sum_local_fy[atomj] = loco_fy_value;
               sum_local_fz[atomj] = loco_fz_value;

               myatoms->fx[atomj] -= fterm * xxi;
               myatoms->fy[atomj] -= fterm * yyi;
               myatoms->fz[atomj] -= fterm * zzi;
            
            }
         }
         /*
         elif (atomi == atomj)
         {
            sum_local_pot[atomj] = 0.0;
            sum_local_vir[atomj] = 0.0;

            sum_local_fx[atomj] = 0.0;
            sum_local_fy[atomj] = 0.0;
            sum_local_fz[atomj] = 0.0;
         }
         */

      } 

      
      
      for (i = 0; i < myatoms->N ; i++)
      { 
         //Sum over all the local potential energies. 
         sum_loco_pot_total += sum_local_pot[i];
         sum_loco_vir_total += sum_local_vir[i];

         
         sum_loco_fx_total += sum_local_fx[i];
         sum_loco_fy_total += sum_local_fy[i];
         sum_loco_fz_total += sum_local_fz[i];
         
      }   

      sum_pot_total += sum_loco_pot_total;
      sum_vir_total += sum_loco_vir_total;
      
      myatoms -> fx[atomi] += sum_loco_fx_total;
      myatoms -> fy[atomi] += sum_loco_fy_total;
      myatoms -> fz[atomi] += sum_loco_fz_total;
   }

   myatoms -> pot_energy = 0.5*sum_pot_total;
   myatoms -> virial = 0.5*sum_vir_total;


   for (atomi=0; atomi < myatoms->N; atomi++)
   {
      myatoms->fx[atomi] *= 24.0 * len_jo->eps;
      myatoms->fy[atomi] *= 24.0 * len_jo->eps;
      myatoms->fz[atomi] *= 24.0 * len_jo->eps;
   }
   myatoms->pot_energy *= 4.0 * len_jo->eps;
   myatoms->virial *= 24.0 * len_jo->eps;
   timeit(1,1);

}

//**********************************************************************
// minimum_image() function
//   - Finds the nearest images of atom i and j, and returns distance.
//   - Arguments:
//       - dist: 1d distance between atoms i and j in central sim. cell.
//       - box_length: length of simulation cell.
//       - half_box_length: half of length of simulation cell.
//**********************************************************************
float minimum_image( const float dist, const float box_length, 
                     const float half_box_length )
{

   float min_dist = dist;
   if (dist > half_box_length ) min_dist = dist - box_length; 
   if (dist < -half_box_length ) min_dist = dist + box_length;
   return min_dist; 

}