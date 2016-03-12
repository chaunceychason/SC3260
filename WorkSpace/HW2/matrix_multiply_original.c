//*****************************************************************************
//
// This program calculates the product of a square matrix with itself:
//
// B = A * A
//
// Please keep all code in this single file.
//
//
//*****************************************************************************

#include <stdio.h>
#include <stdlib.h>

void read_data_function(FILE *file_in, int n_count, int *func_matrix);

void square_matrix(int *matA ,int n_1d, int *matB);

void print_array(int *print_matrix, int nlength );

int main(int argc, char ** argv)
{
   
   // check command line arguments
   if ( argc != 3 ) {
      printf("This program computes the product of n x n matrix with itself\n");
      printf("Usage: ./matrix_multiply filename n\n");
      exit(0);
   }

   // TODO: parse input arguments
   // argv captures each argument in an array of characters
   // Here we loop over all arguments and print the value
   int i;
   for (i=0;i<argc;i++) {
      // %d is for integers, %s is for an array of characters
      printf("i: %d argv[i]: %s\n",i,argv[i]); 
   }
	
   // parses the input arguments and converts to appropiate type. 
   i = 1;
   int myarg_int = 0;
   char *myarg_str = argv[i];
   
   //Sets variables for the input arguments. 
   if ( i == 1 ) myarg_str = argv[i];
   ++i; 
   if ( i == 2 ) myarg_int = atoi(argv[i]);

   //Opens file to read elements for building matrix A.
   FILE *fp_in;
   fp_in = fopen(myarg_str ,"r");
   
   // it's good practice to check whether the file
   // was actually opened successfully. fopen() will
   // fail if the file does not exist, for instance.
   if ( fp_in == NULL ) {
      printf("input_file.txt not opened, exiting...\n");
      exit(0);
   }


   // TODO: dynamically allocate space for matrix_A (input matrix) in 1d array
   int n = myarg_int * myarg_int;
   int * matrix_A;  // declare input matrix;
   matrix_A = malloc( n * sizeof(int) );

   // it's good practice to check that the array was
   // allocated correctly. Doing this by checking for
   // a NULL pointer.
   if ( matrix_A == NULL ) {
      printf("Allocation failed, exiting!\n");
      exit(0);
   }

   // TODO: call function to read data from file and copy into matrix_A
   // fill and access your dynamic array like any
   // other "normal" array

   //BUILDS MATRIX A!
   read_data_function(fp_in, n, matrix_A);
   //Checks Matrix A! print loop
   for ( i=0; i<n ; i++ ) {
      //fscanf(fp_in, "%d", &matrix_A[i] );
      printf("i: %d, matrix_A[i]: %d\n",i, matrix_A[i]);
   }
   printf("\n");

   // TODO: dynamically allocate space for matrix_B (output matrix) in 1d array
   int * matrix_B;  // declare output matrix
   matrix_B = malloc( n * sizeof(int) );

   // Check that the array was allocated correctly. Doing this by checking for
   // a NULL pointer.
   if ( matrix_A == NULL ) {
      printf("Allocation failed, exiting!\n");
      exit(0);
   }
   
   // TODO: call function to perform matrix multiplication ( matrix_B = matrix_A * matrix_A )
   square_matrix(matrix_A, myarg_int, matrix_B);   

   
   // TODO: call function to write results (matrix_B) to stdout
   printf("ABOUT TO PRINT ARRAY! ENTERING FUNCTION...\n");
   printf("==========================================\n");
   print_array(matrix_B, myarg_int);

   // TODO: free space allocated for matrix_A and matrix_B
   free(matrix_A);
   free(matrix_B);

   //CLOSE FILES!
   fclose(fp_in);
   printf("\nClosing file!\n");   

   return 0;

}

void square_matrix(int *matA ,int n_1d, int *matB){
   // This squares matrixA and modifies matrixB. Both are
   // 1-D matrixes of dimension nxn.  
   int i;
   int j;
   int k;
   int new_val;
   int tempval;

   //NESTED LOOP: to compute matA*matA on a 1D matrix of length n_1d
   //ROWS!
   for(j = 0; j<n_1d; j++){
      //PLACEHOLDER FOR xn.
      for(k = 0; k<n_1d; k++){
         new_val = 0;
         //COLUMNS!
         for(i = 0; i<n_1d; i++){
            tempval = matA[j*n_1d+i]*matA[i*n_1d+k];
            new_val = new_val+ tempval;	 
         }
         matB[k + j*n_1d] = new_val;
      }  
   }
}

void read_data_function(FILE *file_in, int n_count, int *func_matrix) { 
   int i;
   for(i=0; i<n_count; i++) {
      fscanf(file_in, "%d", &func_matrix[i] );
   }
}


void print_array(int *print_matrix, int nlength ){
   //Checks Matrix B! print in loop
   int i;
   int n2 = nlength*nlength;
   for ( i=0; i<n2 ; i++ ) {
      //printf("i: %d, print_matrix[i]: %d\n",i, print_matrix[i]);
      printf("%d ", print_matrix[i]);
      if((i+1)%nlength==0) printf("\n");
   }
}
