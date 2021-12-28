from django.http import HttpResponse
from django.template.loader import render_to_string

from django.conf import settings

#! Secret Key Attack/Protection
from django.core import signing
import secrets
import string
pun = "!#$%&()*-.:;<=>?@[]^_`{|}~"
#! secret_key_generator = ''.join(secrets.choice(string.ascii_lowercase + pun + string.digits + string.ascii_uppercase)for i in range(100))

signer = signing.Signer()
def secret_key_page(request):
    """
    !Secret Key is used to provide CRYPTOGRAPHIC signing, should be set to a unique, unpredictable value and should be kept a secret.
    """
    secret_key = "!ghDjA`RzqX{tFE6U]^rnrZTy6Ouug4q?3C$|~@x;VVF`iuI&p5h&.L:kmKK!X:egZnmx~:P%]@;9&Jl?$$xp)W4qvJ{jrbZi-<f"
    signed = signer.sign(secret_key) #! Signing Secret Key
    # signed += '!' #! Tampering with Secret Key
    try:
        original = signer.unsign(signed)
    except signing.BadSignature:
        raise Exception('Secret Key Tampering Detected!')

    context = {
        'secret_key': signed,
        'settings_secret_key': settings.SECRET_KEY
    }
    rendered = render_to_string('security/security_page.html', context)
    return HttpResponse(rendered)

#! Pickling/Serialization Attack/Protection
def pickling_page(request):
    """
    ! If the SECRET_KEY is not kept secret and you are using the PickleSerializer, 
    ! this can lead to arbitrary remote code execution.
    """
    # import pickle
    # import json
    # serialized = pickle.loads('{"name":"Kennedy Gitonga"}')
    # serialized = json.loads('{"name":"Kennedy Gitonga"}')
    from django.contrib.sessions.serializers import PickleSerializer
    from django.core.signing import JSONSerializer

    secret_key = "!ghDjA`RzqX{tFE6U]^rnrZTy6Ouug4q?3C$|~@x;VVF`iuI&p5h&.L:kmKK!X:egZnmx~:P%]@;9&Jl?$$xp)W4qvJ{jrbZi-<f"
    if not request.session.get('name'):
        sess = request.session['name'] = 'Kennedy Gitonga'
    sess = request.session['name'] 

    signed = signing.Signer(secret_key)
    sess_signed = {"desc":"I'm Ken"}
    attack = 'This is pages simulates a simple pickle attack and prevention'

    data = signing.loads(
        sess_signed,
        key=secret_key,
        salt='django.core.signing',
        serializer=PickleSerializer,
        max_age=300,
    )
    context = {
        'session': sess,
        'attack': attack,
        'data': 'data',
    }
    cryptographic_signing()
    rendered = render_to_string('security/security_page_pickle.html', context)
    return HttpResponse(rendered)

def cryptographic_signing():
    #! Protecting a tuple or a list
    #! BY DEFAULT Signer class uses the SECRET_KEY in setting to generate signatures. 
    # ! You can use a different secret key by passing it to the Signer Constructor

    # WzEsMiwzLDQsNV0:ziSt1ys-6LQSuHtf3AwZ0z6WTOU0r8XCxJ6P4yQUccM -> settings.SECRET_KEY
    # WzEsMiwzLDQsNV0:MYmRFep9OTh_VEoh_SIiOVKIiQNKX4geLrH5qJ3uGok -> secret_key

    secret_key = "!ghDjA`RzqX{tFE6U]^rnrZTy6Ouug4q?3C$|~@x;VVF`iuI&p5h&.L:kmKK!X:egZnmx~:P%]@;9&Jl?$$xp)W4qvJ{jrbZi-<f"
    signer = signing.Signer(secret_key)
    signed = signer.sign_object([1, 2, 3, 4, 5])
    unsigned =  signer.unsign_object(signed)
    #! Checking is a signe has be altered
    try:
        unsign =signer.unsign(signed)
    except signing.BadSignature:
        raise Exception('Tampering detected!')

    print(signed)








#! XSS -> Cross Site Scripting Attack/Protection

#! CSRF -> Cross Site Request Forgery Attack/Protection

#! SQL Injection Attack/Protection

#! Clickjacking Attack/Protection

#! Session