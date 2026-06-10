from django.shortcuts import redirect


def commissioner_or_zone_officer(view_func):

    def wrapper(request, *args, **kwargs):

        profile = request.user.userprofile

        if profile.role in [
            'Commissioner',
            'Zone Officer'
        ]:

            return view_func(
                request,
                *args,
                **kwargs
            )

        return redirect(
            '/waste-collection/'
        )

    return wrapper


def operator_only(view_func):

    def wrapper(request, *args, **kwargs):

        profile = request.user.userprofile

        if profile.role == 'Data Entry Operator':

            return view_func(
                request,
                *args,
                **kwargs
            )

        return redirect('/')

    return wrapper