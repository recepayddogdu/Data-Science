select * from CUSTOMER
where CITY='Rize' and DISTRICT='Fýndýklý' -- Rize ve Fýndýklý olanlarý getirir.
-----------------------------------------------------
select*from CUSTOMER
where CITY='Rize' and DISTRICT<>'Fýndýklý' -- Fýndýklý dýþýnda ama Rize olanlarý getirir.
-----------------------------------------------------
select*from CUSTOMER
where AGE>77 --Yaþý 77'den büyük olanlarý getirir.
-----------------------------------------------------
select*from CUSTOMER
where CUSTOMERNAME like 'Recep%' --Ýsmi recep ile baþlayanlar
------------------------------------------------------
select*from CUSTOMER
where CUSTOMERNAME like '%ece%' --Ýsminin içinde ece kelimesi geçenler
----------------------------------------------------------------------
select*from CUSTOMER
where AGE between 20 and 24 --yaþý 20 ile 24 arasýndakiler gelir
----------------------------------------------------------------------
select*from CUSTOMER
where CITY ='ýsparta' and DISTRICT not in ('uluborlu','yalvaç','gelendost') and GENDER='K' 
-- ýsparta'da uluborlu,yalvaç,gelendost ilçeleri dýþýnda oturan kadýnlar.
-----------------------------------------------------------------------------
delete from CUSTOMER where ID=1 --ID'si 1 olan customer'i sil.
select*from CUSTOMER
-----------------------------------------------------------------------
delete from CUSTOMER where CUSTOMERNAME like 'Serhat%' --Ýsmi serhat ile baþlayan customer'lari sil.
select*from CUSTOMER
---------------------------------------------------------------
update CUSTOMER set GENDER='Erkek'
where GENDER='E'

update CUSTOMER set GENDER='Kadýn'
where GENDER='K'

select*from CUSTOMER
-----------------------------------------
insert into CUSTOMER (CUSTOMERNAME,CITY,DISTRICT,BIRTHDATE,GENDER,AGE)
values ('Serdar ÇAKIR','Ýstanbul','Bayrampaþa','1999-12-11','Erkek','20')
select*from CUSTOMER
---------------------------------------------
select*from CUSTOMER
where CUSTOMERNAME like '[a-d]%' --a veya b veya c veya d harfi ile baslayanlari getirir.
-------------------------------------