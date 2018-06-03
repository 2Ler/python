class employee:
  def input_details(self):
    self.name = raw_input("Enter name :")
    self.id = input("Enter ID :")
    self.salary = input("Enter salary")
  def output_details(self):
    print "Name :",self.name
    print "ID :",self.id
    print "Salary :",self.salary
e = employee()
e.input_details()
e.output_details()
