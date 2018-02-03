def students():
    python=['santhi','rama','satya','karthik']
    webapplication=['santhi','rama','santhosh']
    vu=list(set(python).intersection(set(webapplication)))
    print('common students in both python and web application are %s'% vu)
    d=list(set(python).union(set(webapplication)))
    c=list(set(d).difference(set(vu)))
    print('the list of students who are not common in both the classes are %s' % c)
students()