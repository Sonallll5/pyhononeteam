class Employee:
    def read_data(self,ename,ecode,ebs):
        self.emp_name=ename
        self.emp_code=ecode
        self.emp_basics=ebs
    def calculate(self):
        if self.emp_basic<10000:
            self.emp_da=self.emp_basic*0.2
            self.emp_hra=self.emp_basic*0.25
            self.pf=self.emp_basic*0.05
        else:
            self.emp_da=self.emp_basic*0.1
            self.emp_hra=self.emp_basic*0.15
            self.pf=self.emp_basic*0.03
        self.emp_ns=self.emp_basic+self.emp_da+self.emp_hra-self.emp_pf
        def
