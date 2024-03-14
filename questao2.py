def fibo(n) -> bool:
  i = 1
  x = 1
  y = 0
  while i <= n :
    f = x + y
    if f == n:
      return True
    y = x
    x = f
    i = i + 1
  return False
  
def main():
  n = int(input())

  if fibo(n) == True:
    print("Esse número pertence à sequência de Fibonnaci")
  else:
    print("Esse número não pertence à sequência de Fibonnaci")
      
main()
