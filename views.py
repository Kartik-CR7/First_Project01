from django.shortcuts import render

# Create your views here.
def firstpage(req):
    return render(req,'firstpage.html')
#
# def index(request):
#     likebutton = request.POST.get('like')
#     if likebutton:
#         context = {'likebuttton': likebutton}
#         return render(request,'firstpage.html',context)


def result(request):
    name = request.get['q']
    hit = request.session.get('like')
    if not hit:
        request.session['like'] = 1
    else:
        request.session['like'] += 1
    return render(request, 'firstpage.html', {'message': message})
