#%%
class Array_seq:
    def __init__(self):
        self.A=[]
        self.size =0
    def __len__(self):  return self.size
    def __iter__(self): yield from self.A
    def build(self,X):
        self.A = [a for a in X]
        self.size = len(self.A)
    
    def get_at(self,i):
        return self.A[i]
    def set_at(self,i,x):
        self.A[i]=x
    def _copy_forward(self,i,n,A,j):
        for k in range(n):
            A[j+k]=self.A[i+k]
    def _copy_backward(self,i,n,A,j):
        for k in range(n-1,-1,-1):
            A[j+k]=self.A[i+k]
    def insert_at(self,i,x):
        n=len(self)
        A=[None]*(n+1)
        self._copy_forward(0,i,A,0)
        A[i]=x
        self._copy_forward(i,n-i,A,i+1)
        self.build(A)
    def delete_at(self,i):
        n=len(self)
        A = [None]*(n-1)
        self._copy_forward(0,i,A,0)
        x=self.A[i]
        self._copy_forward(i+1,n-i-1,A,i)
        self.build(A)
        return x
    
    def insert_first(self,x):
        self.insert_at(0,x)
    def delete_first(self):
        return self.delete_at(0)
    def insert_last(self,x):
        self.insert_at(len(self),x)
    def delete_last(self):
        return self.delete_at(len(self)-1)

 #%%   
seq = Array_seq()
seq.build([10,20,30])
print("Initial array: ",list(seq))


# %%
print("Item at index 1:", seq.get_at(1))
seq.set_at(1,99)
print("After set_at(1,99): ",list(seq))
# %%
seq.insert_first(5)
print("After insert_first(5):", list(seq))
# %%
seq.insert_last(40)
print("After insert_last(40):", list(seq))
# %%
seq.insert_at(2, 77)  # Insert 77 at index 2
print("After insert_at(2, 77):", list(seq))
# %%
removed_first = seq.delete_first()
print(f"Removed first item ({removed_first}):", list(seq))  # Output: [10, 77, 99, 30, 40]
# %%
removed_last = seq.delete_last()
print(f"Removed last item ({removed_last}):", list(seq))
# %%
removed_mid = seq.delete_at(1)
print(f"Removed item at index 1 ({removed_mid}):", list(seq))  # Output: [10, 99, 30]

# %%
print("Final sequence length:", len(seq))
# %%
