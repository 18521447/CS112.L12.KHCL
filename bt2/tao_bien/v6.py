# #include <map>
# #include <iostream>
# using namespace std;

# #define long long long
# const long M = 1000000007; // modulo
# map<long, long> F;

# long f(long n) {
# 	if (F.count(n)) return F[n];
# 	long k=n/2;
# 	if (n%2==0) { // n=2*k
# 		return F[n] = (f(k)*f(k) + f(k-1)*f(k-1)) % M;
# 	} else { // n=2*k+1
# 		return F[n] = (f(k)*f(k+1) + f(k-1)*f(k)) % M;
# 	}
# }

# main(){
# 	long n;
# 	F[0]=F[1]=1;
# 	while (cin >> n)
# 	cout << (n==0 ? 0 : f(n-1)) << endl;
# }
MOD = 10 ** 9 + 7

def main_fib(n):
	if n == 0 or n == -1:
		return (0, 1)
	else:
		a, b = main_fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)

def fib(n):
	return main_fib(n)[1]

def interleaving_fib(n):
    return fib(n * 2 - 1)


def main(n, k):
    total = 0
    for i in range(k + 1):
        total = (total + interleaving_fib(i)) % MOD
        
    return n * total % MOD

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    print(main(n, k))
