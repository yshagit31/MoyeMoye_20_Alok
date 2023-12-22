from django.shortcuts import render,redirect
from AppName.utils import data
# Create your views here.
def home(request):

    return render(request,'home.html')

def managetaskadd(request):
    if request.method == 'POST':
        category = request.POST.get('Category', '')
        heading = request.POST.get('heading', '')
        date = request.POST.get('date', '')
        status = request.POST.get('status', '')
        description = request.POST.get('description', '')
        form_data = {
            'Category': category,
            'task': heading,
            'due_date': date,
            'status': status,
            'description': description,
        }
        DatabaseSelected = request.session.get('current_database', 'alok')
        data.AddDataInDataBase(form_data,DatabaseSelected)
        return redirect('dashboard')
        
    return render(request,'managetaskadd.html')

def managetaskdelete(request):
    if request.method=='POST':
        selected_options_to_delete = {
            'work_todo': request.POST.getlist('checkbox_options_Work'),
            'personal_todo': request.POST.getlist('checkbox_options_Personal'),
            'skill_todo': request.POST.getlist('checkbox_options_Skill'),
            'shopping_todo': request.POST.getlist('checkbox_options_Shopping'),
        }
        DatabaseSelected = request.session.get('current_database', 'alok')
        data.DeleteDataInDataBase(selected_options_to_delete,DatabaseSelected)
        return redirect('dashboard')


    DatabaseSelected = request.session.get('current_database', 'alok')
    alldata=data.getAllTableDataFromDatabase(DatabaseSelected)
    WorkTableData=alldata["Work"]
    SkillTableData=alldata["Skill"]
    PersonalTableData=alldata["Personal"]
    ShoppingTableData=alldata["Shopping"]
    return render(request,'managetaskdelete.html',{"worktabledata":WorkTableData,"personaltabledata":PersonalTableData,"shoppingtabledata":ShoppingTableData,"skilltabledata":SkillTableData})

def managetaskupdate(request):
    return render(request,'managetaskupdate.html')

def dashboard(request):
    DatabaseSelected = request.session.get('current_database', 'alok')
    alldata=data.getAllTableDataFromDatabase(DatabaseSelected)
    WorkTableData=alldata["Work"]
    SkillTableData=alldata["Skill"]
    PersonalTableData=alldata["Personal"]
    ShoppingTableData=alldata["Shopping"]
    return render(request,'dashboard.html',{"worktabledata":WorkTableData,"personaltabledata":PersonalTableData,"shoppingtabledata":ShoppingTableData,"skilltabledata":SkillTableData})

def user_login(request):
    selected_database='alok'
    request.session['current_database'] = selected_database
    return render(request,'user_login.html')

