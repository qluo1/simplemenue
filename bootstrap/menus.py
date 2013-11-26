from django.core.urlresolvers import reverse

from menu import Menu, MenuItem

def profile_title(request):
    """
    Return a personalized title for our profile menu item
    """
    # we don't need to check if the user is authenticated because our menu
    # item will have a check that does that for us
    name = request.user.get_full_name() or request.user

    return "%s's Profile" % name

Menu.add_item("main", MenuItem("Home",
                               reverse("Home")))

Menu.add_item("main", MenuItem("Product",
                               reverse("Product")))

Menu.add_item("main", MenuItem("Services",
                               reverse("Services")))

Menu.add_item("main", MenuItem("About",
                               reverse("About")))

Menu.add_item("main", MenuItem("Contact",
                               reverse("Contact")))
