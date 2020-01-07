# Django
from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as user_model

# local Django
from .models import GroupMember, Gift, UserGroup
from .forms import AddGift, AddGroupMember

@login_required(login_url='/accounts/login/')
def home(request):
    """
    Displays and creates instances of :model:`giftlist.Gift` that belong to the current user.

    **Context**

    ``add_gift_form``
        Instance of :form:`giftlist.AddGift` which allow users to create a new instance of :model:`giftlist.Gift`.

    ``new_gift``
        Instance of :model:`giftlist.Gift` posted by add_gift_form.

    ``user_groups``
        Query set of :model:`giftlist.GroupMember` which contains all the groups that the current user in.

    ``gifts``
        Query set of :model:`giftlist.Gift` that belongs to the current user.

    **Template:**

    :template:`giftlist/home.html`
    """

    if request.method == 'POST':

        add_gift_form = AddGift(request.POST)

        if add_gift_form.is_valid():
            new_gift = add_gift_form.save()
            new_gift.save()
            return redirect('giftlist:home')

    else:
        user = request.user
        user_groups = GroupMember.objects.filter(member=user)
        gifts = Gift.objects.filter(user=user)
        add_gift_form = AddGift()
        context = {'groups':user_groups,'gifts': gifts, 'add_gift_form': add_gift_form}
        return render(request, 'giftlist/home.html', context)

def groupResults(request):
    """
    Return search results of groups
    **Context**

    ``user``
        Instance of user that is currently logged in.

    ``form``
        Instance of :form:`forms.AddGroupMember`.

    ``group_member``
        Instance of :model:`models.GroupMember`

    **Template:**

    :template:`user/templates/group/home.html`
    """
    user = request.user

    if request.method == 'POST':
        user = request.user
        form = AddGroupMember(request.POST)
        if form.is_valid():
            group_member = form.save(commit=False)
            group_member.member = user
            group_member.save()
            return redirect('giftlist:home')


    else:
        form = AddGroupMember()
        query = request.GET.get('q')
        results = UserGroup.objects.filter(Q(group_name__icontains=query))
        context = {'form': form, 'results': results}
        return render(request, 'group/groupresults.html', context)

def addGroup(request):
    return redirect('giftlist:home')

def groupLlist(request):
    """
    Return a list of users that belong to a certain group.
    **Context**

    ``group_id``
        ID of the group that is being looked up

    ``members``
        A query set of all the users of the group.

    **Template:**

    :template:`giftlist/group/grouplist.html`
    """
    group_id = UserGroup.objects.filter(group_name='Family')
    members = GroupMember.objects.filter(group=group_id[0].id)
    print(group_id[0].id)

    context = {'members': members}
    return render(request, 'giftlist/grouplist.html', context)

def memberGiftList(request, User):
    """
    Returns the gift list of a user in a group.

    **Context**

    ``member``
        Instance of User

    ``person``
        Query set of the user's list that is being looked up

    ``gifts``
        Query set of the gifts that belong to the user of the group.
    """
    member = User
    print("this member was sent thru the url:"+ member)

    person = user_model.objects.get(username="{0}".format(str(member)))
    print("I got this user from my query: {0}".format(person.id))
    gifts = Gift.objects.filter(user=person.id)
    context = {'member': member, 'gifts': gifts}
    return render(request, 'giftlist/membergiftlist.html', context)
