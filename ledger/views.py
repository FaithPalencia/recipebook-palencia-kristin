from .models import Recipe
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import RecipeImage

# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name', 'author']
    template_name = 'ledger/recipe_add.html'
    success_url = reverse_lazy("recipe_list")

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    fields = ['image','description']
    template_name = "ledger/image_add.html"

    def form_valid(self, form):
        form.instance.recipe_id = self.kwargs['pk']
        return super().form_valid(form)