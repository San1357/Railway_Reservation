to run this project you have to follow this command

You have to make some changes:

 
   * $ ls /etc/postgresql/9.5/main/postgresql.conf
   then type 
   * $ nano /etc/postgresql/9.5/main/postgresql.conf  #(if this not work then add sudo into it)
                or 
     $ sudo nano /etc/postgresql/9.5/main/postgresql.conf

   * Now, IN CONNECTION AND AUTHENTICATION change the listen address = "*" & Remove the "#" 
      after that & IN FILE LOCATION copy the file location of hba_file which look somewhat
      like this: hba_file = '/etc/postgresql/9.5/main/pg_hba.conf

   * $ sudo nano /etc/postgresql/9.5/main/pg_hba.conf 
      Now at very end of the file uncomment the last line & do change the address to 0.0.0.0/0
      & save it.
        
       
      then restart psql by this command
       
   * $ sudo /etc/init.d/postgresql restart

after folowing this, Now  build & run the docker file (follow step given below) & run the python file . 

       
       

step 1: first build image of the docker file viz named as "Dockerfile"
        $ docker build -t ubuntu_py3.6 .  #image name

step 2: then run the docker file.
        $ docker run -it --rm --add-host="localhost:"your ip address" -p 5000:5000 --name demo ubuntu_py3.6 bash

step3: run the api file 
       $ python api_filename




