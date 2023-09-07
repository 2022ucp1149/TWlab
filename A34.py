def gross_sal(basic,grade):
	HRA=0.20*basic
	DA=0.50*basic
	PF=0.11*basic;
	if(grade=='A'):
		Allow=1700;
	if(grade=='B'):
		Allow=1500;
	if(grade=='C'):
		Allow=1300;
	gross=basic+HRA+DA+Allow-PF;
	print("Gross salary: ",gross)
	return

gross_sal(10000,'A')
gross_sal(4567,'B')
