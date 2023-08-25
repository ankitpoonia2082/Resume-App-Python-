from django.shortcuts import render

# Create your views here.

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        purpose = request.POST.get('purpose')

        context ={'name':name}

        return render(request , 'thanks.html',context)

    return render(request , 'contact.html')

def skills_view(request):
    skills = {
        'Python' : 90,
        'JavaScript': 70,
        'JQuery': 50,
        'HTML': 60,
        'CSS': 75,
        'SQL': 65,
        'Django': 80,
        'BootStrap': 50,
    }
    context ={'skills':skills}

    return render(request , 'skills.html',context)


def project_view(request):

    pro={
        'project1':{'Sr.no':1 ,'name':'Bank Management System', 'Languages':'Python,SQL','desc':'This application is made using python language and SQL (for storing data).In this application have 3 sections(admin login ,User login and user registration section).Admin can add or remove user and update accounts. In user section user can "check balance, add amount, widrawl amount, user can take loan and user can view transaction history".Apllication uses RegEx for validation/checking or user registration data'},
        'project2':{'Sr.no':2 ,'name':'Library Management System', 'Languages':'Python,SQL,RegEx','desc':'This application is made using python language and SQL (for storing data).In this application have 2 sections(admin Section ,User section).Admin can see all books,add books or remove books and can remove users. In user section user have 2 options login or register (registration data is checked/validated using RegEx) user can "See all books, borrow books, search for book by using book name or auther name.'},
        'project3':{'Sr.no':3 ,'name':'Food Dilivery Application', 'Languages':'Python,SQL','desc':'In this application we have 3 sections(admin login ,User login and user registration section).Admin can see menu, add or remove food item from menu and delete user accounts. In user login section user can see menu, search for food, see food price, order food with selecting amount of item, delete account, update account and can view order history.'},
    }

    context={'pro':pro}

    return render(request,'project.html',context)


def experience_view(request):

    exp={
        'Python':'1 year experiance in core python programing.',
        'SQL':' 1 year Intermediate level experiance in using SQL querys and SQL connectivity.',
        'HTML, CSS':'6 months of experiance of using HTML and CSS.',
    }

    context={'exp':exp}
    
    return render(request, 'experience.html', context)

def qualification_view(request):
    study ={ 
        'SSC':{'Sr':1,'Study':'SSC', 'Board':'HBSE','Marks':'66%', 'Year of passing':2015},
        'HSC':{'Sr':2,'Study':'HSC', 'Board':'HBSE','Marks':'52%', 'Year of passing':2017},
        'Diploma':{'Sr':3,'Study':'Diploma in Computer Engineering', 'Board':'HSBTE','Marks':'59%', 'Year of passing':2020},
        'BCA':{'Sr':4,'Study':'BCA', 'Board':'Swami Vivekanand Subharti University','Marks':'65%','Year of passing':2023},
    }
    

    context = {'study':study}
    return render(request,'qualification.html',context)
