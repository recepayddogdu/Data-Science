select top 5 * from CUSTOMER --ilk 5 sonucu listeler
where CITY='istanbul'
order by CUSTOMERNAME
---------------------------
select top 50 percent*from CUSTOMER --yuzde 50'sini listeler
order by CUSTOMERNAME