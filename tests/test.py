from dependencyfixer import fix
dep=['hgdjgjgv']
print("############Trying nonverbose and invalid with auto")
fix(dep)
dep.append('as')
print("############Trying Verbose and invalid with auto")
fix(dep,verbose=True)
print("##############Trying nonverbose and invalid with auto FASLE STAGE 1 :YES")
fix(dep,auto=False)
print("##############Trying nonverbose and invalid with auto FASLE STAGE 1 :NO")
fix(dep,auto=False)
print("###############Trying nonverbose and invalid with auto,instant Kill")
fix(dep,instantkill=True)