<?php 
   $host_name = 'localhost';
   $db_user = 'root';
   $db_pass = '';
   $db_name = 'your tutor';
   
   $con = mysqli_connect($host_name,$db_user,$db_pass,$db_name); 
   
   if(!$con){
       die("something went wrong");
   }  
   
    ?>