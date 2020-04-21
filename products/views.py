from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from accounts.models import Votes
from django.utils import timezone

def home(request):
	products = Product.objects
	return render(request, 'products/home.html', {'products': products})

def create(request):
	if request.method == 'POST':
		product = Product()
		product.title = request.POST['Title']
		product.body = request.POST['Body']
		product.url = request.POST['Url']
		product.icon = request.FILES['Icon']
		product.image = request.FILES['Image']
		product.pub_date = timezone.datetime.now()
		product.votes_total = 1
		product.hunter = request.user
		product.save()
		new_product_vote = Votes()
		new_product_vote.voter = request.user
		new_product_vote.product = product
		new_product_vote.save()
		return redirect('/products/' + str(product.id))
	else:
		return render(request, 'products/create.html')

def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'products/detail.html', {'product': product})

@login_required(login_url='/accounts/signup/')
def upvote(request, product_id):
	if request.method == 'POST':
		try:
			existing_product = get_object_or_404(Product, pk=product_id)
			product_vote = get_object_or_404(Votes, product=existing_product, voter=request.user)
			return render(request, 'products/detail.html', {'product': existing_product, 'restrict': 'You have already voted this product.'})
		except:
			existing_product.votes_total += 1
			existing_product.save()
			new_product_vote = Votes()
			new_product_vote.voter = request.user
			new_product_vote.product = existing_product
			new_product_vote.save()
			return redirect('/products/' + str(product_id)) 