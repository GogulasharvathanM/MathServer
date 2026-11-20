from django.shortcuts import render
def churn_rate(request):
    i_c= float(request.POST.get('Initial_Cust', '0'))
    p_c=float(request.POST.get('Present_Cust', '0'))
    churn = i_c/p_c if request.method=='POST' else 0
    print("Initial Customer =",i_c)
    print("Present Customer =",p_c)
    print("Churn Rate =",churn)
    return render(request, 'mylove/gogul.html',{'i_c': i_c, 'p_c': p_c, 'churn': churn})