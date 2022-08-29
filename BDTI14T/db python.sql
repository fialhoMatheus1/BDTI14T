create database dbTI14TPython;
use dbTI14TPython;

create table pessoa(
	codigo int not null primary key auto_increment,
    nome varchar(120) not null,
    telefone varchar(15) not null,
    endereco varchar(220) not null,
    dataDeNascimento date not null
) engine = InnoDB;

select * from pessoa;