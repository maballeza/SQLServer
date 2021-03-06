### Description:
A script querying the Azure SQL Database sample, [*Adventure Works*](https://docs.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver15&tabs=ssms), for the products sold based on the state in which the sale took place. It requires as an argument the abbreviation of the state of interest.

### Example:
The following command:
```CMD
>python salebystate.py --st NM
```
gives the result:
```CMD
State                   Product Name
New Mexico              Touring-3000 Blue, 50
New Mexico              Touring-3000 Yellow, 50
New Mexico              Touring-2000 Blue, 60
New Mexico              Long-Sleeve Logo Jersey, L
New Mexico              Short-Sleeve Classic Jersey, L
New Mexico              Touring-1000 Yellow, 60
New Mexico              Touring-3000 Yellow, 62
New Mexico              Chain
New Mexico              Front Brakes
New Mexico              Front Derailleur
New Mexico              Touring-2000 Blue, 54
New Mexico              Bike Wash - Dissolver
New Mexico              Touring-3000 Blue, 54
New Mexico              Touring-1000 Blue, 60
New Mexico              Touring-3000 Yellow, 44
New Mexico              Touring-1000 Blue, 46
New Mexico              AWC Logo Cap
```

##### Note:
Running the script requires the creation of an [Azure SQL Database](https://docs.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver15&tabs=ssms).