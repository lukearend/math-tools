import base64, codecs 
sad = '\x72\x6f\x74\x31\x33'
gardo = 'aW1wb3J0IG51bXB5IGFzIG5wCmltcG9ydCBzY2lweQpmcm9tIHNjaXB5IGltcG9ydCBuZGltYWdlCgpjbGFzcyB1bmtub3duX3N5c3RlbXMob2JqZWN0KToKICAgIGRlZiBfX2luaXRfXyhzZWxmKToKICAgICAgICBzdXBlci5fX2luaXRfXygpCgoKICAgIGRlZiB1bmtub3duX3N5c3RlbV8xKGlucHV0KToKICAgICAgICAjIGNoZWNrIHRoYXQgeCBpcyAgYSA2NC1EIGNvbHVtbiB2ZWN0b3IgKGVycm9yIGlmIG5vdCkKICAgICAgICBOID0gNjQ7CiAgICAgICAgaWYgbGVuKGlucHV0LnNoYXBlKSAhPSAxOgogICAgICAgICAgICBwcmludCgnRXJyb3I6IElucHV0IHNob3VsZCBiZSBhIDEtRCBWZWN0b3Igd2l0aCA2NCBlbnRyaWVzIChzbyBpbnB1dC5zaGFwZSBzaG91bGQgYmUgYSBvbmUtdHVwbGUgKDY0LCkpJyApCiAgICAgICAgICAgIHJldHVybgogICAgICAgIGlmIGlucHV0LnNoYXBlWzBdICE9IE46CiAgICAgICAgICAgIHByaW50KCdFcnJvcjogSW5wdXQgc2hvdWxkIGJlIGEgMS1EIFZlY3RvciB3aXRoIDY0IGVudHJpZXMgKHNvIGlucHV0LnNoYXBlIHNob3VsZCBiZSBhIG9uZS10dXBsZSAoNjQsKSknICkKICAgICAgICAgICAgcmV0dXJuCgogICAgICAgICMgeSA9IGZpbHQgKiAobS4qeCkgLS0+IHN5c3RlbSBpcyBsaW5lYXIgYnV0IG5vdCBzaGlmdCBpbnZhcmlhbnQKICAgICAgICBmaWx0ID0gbnAuYXJyYXkoWy0xLCAyLCAyLCAtMV0pLzQ7CiAgICAgICAgZmlsdCA9IGZpbHQuVAoKICAgICAgICAjIGJ1aWxkIHRoZSBtYXNrCiAgICAgICAgZnIgPSAwLjY7CiAgICAgICAgbWFzayA9IG5wLm9uZXMoTik7CiAgICAgICAgbWFza19yYW5nZSA9IG5wLmFycmF5KHJhbmdl'
tram = 'XP0kXzyhqPuBYmVcYPOcoaDbGv8lXFxcPvNtVPNtVPNtoJSmnlN9VT1up2ftXlOzpvchpP5yrUNbYGRhZPNdVPugLKAeK3WuozqyYyDdXwVcYltlXvuBYmLcXvblXFx7PtbtVPNtVPNtVPZtoJSmnlO0nTHtnJ5jqKDXVPNtVPNtVPOcoaO1qQVtCFOgLKAeVPbtnJ5jqKDXPvNtVPNtVPNtVlOwnKWwqJkupvOwo252o2k1qTyiovOiMvOgLKAeMJDtnJ5jqKDtq2y0nPOznJk0MKVXVPNtVPNtVPOcoaO1qQVtCFOhpP5bp3EuL2fbJ2yhpUI0ZvjtnJ5jqKDlYPOcoaO1qQWqXDbtVPNtVPNtVUWyp3NlVQ0toaNhL29hqz9fqzHbnJ5jqKDlVPkznJk0YPOgo2EyCFqzqJkfWlx7PtbtVPNtVPNtVUEyoKNtCFOhpP56MKWipltlAGLcPvNtVPNtVPNtqTIgpSfjBwR5AI0tCFOlMKAjZtbtVPNtVPNtVUWyp3NlVQ0toaNhrzIlo3ZbAwDcPvNtVPNtVPNtMz9lVTxtnJ4tpzShM2HbAPx6PvNtVPNtVPNtVPNtVT5yrUEsL2u1ozftCFO0MJ1jJ2xdAwD6XTxeZFxdAwEqPvNtVPNtVPNtVPNtVUWyp3NlVQ0tpzImpQVtXlOhMKu0K2AbqJ5ePtbtVPNtVPNtVUWyqUIlovOlMKAjZtbXPvNtVPOxMJLtqJ5eoz93oy9mrKA0MJ1sZvucoaO1qPx6PvNtVPNtVPNtVlOwnTIwnlO0nTS0VUttnKZtVTRtAwDgEPOwo2k1oJ4tqzIwqT9lVPuypaWipvOcMvOho3DcPvNtVPNtVPNtGvN9VQL0BjbtVPNtVPNtVTyzVTkyovucoaO1qP5mnTSjMFxtVG0tZGbXVPNtVPNtVPNtVPNtpUWcoaDbW0Ilpz9lBvOWoaO1qPOmnT91oTDtLzHtLFNkYHDtIzIwqT9lVUqcqTttAwDtMJ50pzyyplNbp28tnJ5jqKDhp2uupTHtp2uiqJkxVTWyVTRto25yYKE1pTkyVPt2APjcXFptXDbtVPNtVPNtVPNtVPOlMKE1pz4XVPNtVPNtVPOcMvOc'
krugz = 'bnB1dC5zaGFwZVswXSAhPSBOOgogICAgICAgICAgICBwcmludCgnRXJyb3I6IElucHV0IHNob3VsZCBiZSBhIDEtRCBWZWN0b3Igd2l0aCA2NCBlbnRyaWVzIChzbyBpbnB1dC5zaGFwZSBzaG91bGQgYmUgYSBvbmUtdHVwbGUgKDY0LCkpJyApCiAgICAgICAgICAgIHJldHVybgoKICAgICAgICAjIHkgPSBmaWx0ICogaW5wdXQgKGxpbmVhciBhbmQgc2hpZnQgaW52YXJpYW50KQogICAgICAgIGZpbHQgPSAwLjcgKyAoLTAuNykqKihucC5hcnJheShyYW5nZSgwLCAxNykpKTsKICAgICAgICBmaWx0ID0gZmlsdC5UCgogICAgICAgIGZ1bGxfaW4gPSBucC5oc3RhY2soW2lucHV0LCBpbnB1dCwgaW5wdXRdKQogICAgICAgIHJlc3AyID0gbnAuY29udm9sdmUoZnVsbF9pbiAsZmlsdCwgbW9kZT0nZnVsbCcpOwogICAgICAgIHJlc3AgPSByZXNwMltOOjIqTl07CgogICAgICAgIHJldHVybiByZXNwCgogICAgZGVmIHVua25vd25fc3lzdGVtXzMoaW5wdXQpOgogICAgICAgICMgY2hlY2sgdGhhdCB4IGlzICBhIDY0LUQgY29sdW1uIHZlY3RvciAoZXJyb3IgaWYgbm90KQoKICAgICAgICBOID0gNjQ7CgogICAgICAgIGlmIGxlbihpbnB1dC5zaGFwZSkgIT0gMToKICAgICAgICAgICAgcHJpbnQoJ0Vycm9yOiBJbnB1dCBzaG91bGQgYmUgYSAxLUQgVmVjdG9yIHdpdGggNjQgZW50cmllcyAoc28gaW5wdXQuc2hhcGUgc2hvdWxkIGJlIGEgb25lLXR1cGxlICg2NCwpKScgKQogICAgICAgICAgICByZXR1cm4KICAgICAgICBpZiBpbnB1dC5zaGFwZVswXSAhPSBOOgogICAgICAgICAgICBwcmludCgnRXJyb3I6IElucHV0IHNob3VsZCBiZSBhIDEtRCBWZWN0b3Igd2l0aCA2NCBlbnRyaWVz'
missy = 'VPumolOcoaO1qP5mnTSjMFOmnT91oTDtLzHtLFOiozHgqUIjoTHtXQL0YPxcWlNcPvNtVPNtVPNtVPNtVUWyqUIlotbXPvNtVPNtVPNtVlOznJk0VPbtJmReqTShnPu4XI0tYFOmnTyzqP1coaMupzyyoaDtLaI0VT5iqPOfnJ5yLKVXVPNtVPNtVPOznJk0VQ0toaNhLKWlLKxbJmRfVQZfVQSqXF5HYmH7PtbXPvNtVPNtVPNtnJ5jqKDlVQ0toaNhqTShnPt0XzyhpUI0VP8toaNhoJS4XSghpP5uLaZboaNhoJS4XTyhpUI0XFxfPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVT5jYzSvpluhpP5gnJ4bnJ5jqKDcXI0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtXDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNcPtbXVPNtVPNtVPNwVUWypUWiMUIwnJ5aVTAcpzA1oTSlVTAioaMioUI0nJ9hVT1iMPNkZNbtVPNtVPNtVTyhpUI0ZvN9VT5jYzumqTSwnluonJ5jqKDlYPOcoaO1qQVfVTyhpUI0Zy0cPvNtVPNtVPNtpzImpQVtCFOhpP5wo252o2k2MFucoaO1qQVtYTMcoUDfVT1iMTH9W2M1oTjaXGfXVPNtVPNtVPO0MJ1jVQ0toaNhrzIlo3ZbZwH2XDbtVPNtVPNtVUEyoKOoZQbkBGEqVQ0tpzImpQVXVPNtVPNtVPOlMKAjZvN9VT5jYacypz9mXQL0XDbtVPNtVPNtVTMipvOcVTyhVUWuozqyXQDcBtbtVPNtVPNtVPNtVPOhMKu0K2AbqJ5eVQ0tqTIgpSgcXwL0BvucXmRcXwL0KDbtVPNtVPNtVPNtVPOlMKAjZvN9VUWyp3NlVPftozI4qS9wnUIhnjbXPvNtVPNtVPNtVlOyrUOiozIhqTyuqTHtpzImqJk0PvNtVPNtVPNtpzImpPN9VT5jYzI4pPtkYwZdpzImpQVcBjbXVPNtVPNtVPOlMKE1pz4tpzImpNb='
ryndo = eval('\x67\x61\x72\x64\x6f') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x74\x72\x61\x6d\x2c\x73\x61\x64\x29')+ eval('\x6b\x72\x75\x67\x7a') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6d\x69\x73\x73\x79\x2c\x73\x61\x64\x29')
eval(compile(base64.b64decode(eval('\x72\x79\x6e\x64\x6f')),'<string>','exec'))

"""
>>> '\x72\x6f\x74\x31\x33'
'rot13'
>>> '\x67\x61\x72\x64\x6f'
'gardo'
>>> '\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x74\x72\x61\x6d\x2c\x73\x61\x64\x29'
'codecs.decode(tram,sad)'
>>> '\x6b\x72\x75\x67\x7a'
'krugz'
>>> '\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6d\x69\x73\x73\x79\x2c\x73\x61\x64\x29'
'codecs.decode(missy,sad)'
>>> '\x72\x79\x6e\x64\x6f'
'ryndo'
>>> 
"""

"""
sad = rot13
eval(
    gardo,         <- b64 encoded
    rot13(tram),   <- rot13 and then b64 encoded
    krugz,         <- b64 encoded
    rot13(missy)   <- rot13 and then 64 encoded
)
"""

"""
import numpy as np
import scipy
from scipy import ndimage

class unknown_systems(object):
    def __init__(self):
        super.__init__()


    def unknown_system_1(input):
        # check that x is  a 64-D column vector (error if not)
        N = 64;
        if len(input.shape) != 1:
            print('Error: Input should be a 1-D Vector with 64 entries (so input.shape should be a one-tuple (64,))' )
            return
        if input.shape[0] != N:
            print('Error: Input should be a 1-D Vector with 64 entries (so input.shape should be a one-tuple (64,))' )
            return

        # y = filt * (m.*x) --> system is linear but not shift invariant
        filt = np.array([-1, 2, 2, -1])/4;
        filt = filt.T

        # build the mask
        fr = 0.6;
        mask = np.ones(N);
        mask_range = np.array(range(-1*int(N/2), int(N/2)))
        mask = mask + fr*np.exp(-1.0 * (mask_range.T**2)/(2*(N/6)**2));

        # mask the input
        input2 = mask * input

        # circular convolution of masked input with filter
        input2 = np.hstack([input2, input2, input2])
        resp2 = np.convolve(input2 ,filt, mode='full');

        temp = np.zeros(256)
        temp[0:195] = resp2
        resp2 = np.zeros(64)
        for i in range(4):
            next_chunk = temp[i*64:(i+1)*64]
            resp2 = resp2 + next_chunk

        return resp2


    def unknown_system_2(input):
        # check that x is  a 64-D column vector (error if not)
        N = 64;
        if len(input.shape) != 1:
            print('Error: Input should be a 1-D Vector with 64 entries (so input.shape should be a one-tuple (64,))' )
            return
        if input.shape[0] != N:
            print('Error: Input should be a 1-D Vector with 64 entries (so input.shape should be a one-tuple (64,))' )
            return

        # y = filt * input (linear and shift invariant)
        filt = 0.7 + (-0.7)**(np.array(range(0, 17)));
        filt = filt.T

        full_in = np.hstack([input, input, input])
        resp2 = np.convolve(full_in ,filt, mode='full');
        resp = resp2[N:2*N];

        return resp

    def unknown_system_3(input):
        # check that x is  a 64-D column vector (error if not)

        N = 64;

        if len(input.shape) != 1:
            print('Error: Input should be a 1-D Vector with 64 entries (so input.shape should be a one-tuple (64,))' )
            return
        if input.shape[0] != N:
            print('Error: Input should be a 1-D Vector with 64 entries (so input.shape should be a one-tuple (64,))' )
            return


        # filt * [1+tanh(x)] - shift-invarient but not linear
        filt = np.array([1, 3, 1]).T/5;



        input2 = np.tanh(4*input / np.max([np.abs(np.max(input)),
                                          np.abs(np.min(input))]
                                          )
                                          )


        # reproducing circular convolution mod 10
        input2 = np.hstack([input2, input2, input2])
        resp2 = np.convolve(input2 ,filt, mode='full');
        temp = np.zeros(256)
        temp[0:194] = resp2
        resp2 = np.zeros(64)
        for i in range(4):
            next_chunk = temp[i*64:(i+1)*64]
            resp2 = resp2 + next_chunk


        # exponentiate result
        resp = np.exp(1.3*resp2);

        return resp
"""