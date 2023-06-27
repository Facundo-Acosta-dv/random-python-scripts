create database persona;

use persona;

create table persona(
    id int not null primary key auto_increment,
    nombre varchar(50) not null,
    edad int(3) not null,
    email varchar(50) unique
);
