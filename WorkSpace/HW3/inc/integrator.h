
#ifndef INTEGRATOR_H
#define INTEGRATOR_H

#include "params.h"
#include "atoms.h"


void update_positions( Atoms *, const misc_params *,  int scounts[], int displs[], int , int );
//void update_positions( Atoms *, const misc_params *);
void update_velocities( Atoms *, const misc_params *, int scounts[], int displs[], int, int );
void pbc( Atoms *, const float, const float );

#endif
