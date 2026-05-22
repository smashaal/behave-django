import sys
import traceback
from behave import given, then
from django.conf import settings


@given("the recursion limit is {headroom:d}")
def set_recursion_limit(context, headroom):
    current_depth = len(traceback.extract_stack())
    sys.setrecursionlimit(current_depth + headroom)


@then("a Django setting can be accessed without error")
def access_django_setting(context):
    _ = settings.DEBUG
