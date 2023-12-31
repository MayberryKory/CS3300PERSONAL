from django.views import generic
from django.views import generic
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Student, Portfolio, Project
from .forms import ProjectForm, PortfolioForm




# Create your views here.
def index(request):
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})

class StudentListView(generic.ListView):
    model = Student

class StudentDetailView(generic.DetailView):
    model = Student

class PortfolioListView(generic.ListView):
    model = Portfolio

class PortfolioDetailView(generic.DetailView):
    model = Portfolio

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio = self.get_object()
        context['projects'] = Project.objects.filter(portfolio=portfolio)
        return context

class ProjectListView(generic.ListView):
    model = Project

class ProjectDetailView(generic.DetailView):
    model = Project   

def createProject(request, portfolio_id):
    form = ProjectForm()
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id
        
        form = ProjectForm(project_data)
        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set the portfolio relationship
            project.portfolio = portfolio
            project.save()

            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)

    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)


def deleteProject(request, portfolio_id, project_id):
    
    project = Project.objects.get(pk=project_id)

    if request.method == 'POST':
        # Delete the project
        project.delete()
        return redirect('portfolio-detail', portfolio_id)

    return render(request, 'portfolio_app/project_delete.html', {'project': project})


def updateProject(request, portfolio_id, project_id):
    
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    
    project = Project.objects.get(pk=project_id, portfolio=portfolio)
    form = ProjectForm(request.POST or None ,instance=project)
    
    
    
    if request.method == 'POST' and form.is_valid():
        project = form.save()
        project.portfolio = portfolio
        project.save()
        return redirect('portfolio-detail', portfolio_id)

    context = {'project': project ,'form': form, }
    return render(request, 'portfolio_app/project_form.html', context)



def updatePortfolio(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    
    form = PortfolioForm(request.POST or None, instance=portfolio)
    
    if request.method == 'POST' and form.is_valid():
        portfolio = form.save()
        
        portfolio.save()
        return redirect('portfolio-detail', portfolio_id)

    context = {'form': form, 'portfolio':portfolio}
    return render(request, 'portfolio_app/project_form.html', context)