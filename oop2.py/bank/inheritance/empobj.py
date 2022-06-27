from empit import EmpIT
from empit import EmpMKT

#create object employee IT
mike = EmpIT('001','mike',60000)
mike.add_skill("Python, JavaScript")
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()


anna = EmpMKT ("002","Anna",35000)
anna.emp_detail()
anna.mkt_salary()

paul = EmpMKT("003","Pual",45000)
paul.add_commission(35)
paul.add_location("Chiang Mai")
paul.emp_detail()
paul.mkt_salary()
