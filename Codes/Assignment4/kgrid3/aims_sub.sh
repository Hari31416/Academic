#/bin/sh
### Set the job name
#PBS -N Graphene
### Set the project name, your department dc by default
#PBS -P physics
#PBS -l select=1:ncpus=8
### Specify "wallclock time" required for this job, hhh:mm:ss
#PBS -l walltime=00:03:00
#PBS -o stdout_file
#PBS -e stderr_file
#PBS -l software=AIMS
#### Get environment variables from submitting shell
# After job starts, must goto working directory. 
# $PBS_O_WORKDIR is the directory from where the job is fired. 

cd $PBS_O_WORKDIR
#job 
module load suite/intel/parallelStudio
time -p mpirun -n $PBS_NTASKS $HOME/bin/aims.052014.scalapack.mpi.x > output

#NOTE
# The job line is an example : users need to suit their applications
# The PBS select statement picks n nodes each having m free processors
# OpenMPI needs more options such as $PBS_NODEFILE
