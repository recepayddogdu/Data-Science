insert into
CUSTOMER
(CUSTOMERNAME,CITY,DISTRICT,BIRTHDATE,GENDER)
values
('AYÇA BÝNGÜL','Ýstanbul','Gaziosmanpasa','1999-06-06','K')
--yeni columns(satirlar) eklemek icin insert kullanilir

update customer
set AGE=DATEDIFF(year,BIRTHDATE,getdate()) --Yasi hesaplar

select * from customer
