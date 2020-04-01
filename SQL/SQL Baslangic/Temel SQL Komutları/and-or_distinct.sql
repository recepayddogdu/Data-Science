select*from CUSTOMER
where CITY='istanbul' and CUSTOMERNAME like 'Hüseyin%' --Istanbul'da yasayan ve ismi Huseyin olan customer'lari getir.
------------------------------------------------------------------
select*from CUSTOMER 
where CITY='istanbul' or CUSTOMERNAME like 'Hüseyin%' --Istanbul'da yasayan veya ismi Huseyin olan customer'lari getir.
----------------------------------------------------
select  CITY from CUSTOMER -- sehirlerin hepsini yazar
--------------------
select distinct CITY from CUSTOMER -- Her sehir ismini bir kere yazar, verilerin tekrar yazilmasini onler.
--------------------------
select distinct CITY,DISTRICT from CUSTOMER where CITY='istanbul' --Istanbuldaki ilceleri siralar.