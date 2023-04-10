a = [13.0 1.96 0.44 0.12];
dim = 4;
Ham = zeros(dim,dim);
Ovl = zeros(dim,dim);

for n = 1:4
    for m =1:4
    Ham(n,m) = v(a(n),a(m))+t(a(n),a(m));
    Ovl(n,m) = p(a(n),a(m));
    end
end

[V,D] = eig(Ham,Ovl);
display(V);
display(D);
nV = [-0.1868*V(1,4) -0.1868*V(2,4) -0.1868*V(3,4) -0.1868*V(4,4)];
x = 0:0.01:3;
eigfunc = nV(1)*exp(-a(1).*x.^2)+nV(2)*exp(-a(2).*x.^2)+nV(3)*exp(-a(3).*x.^2)+nV(4)*exp(-a(4).*x.^2);
plot(x,eigfunc);
ylim([0,0.6]);

%注意此处势能要加入负号，因为课件计算的是<an|(1/r)|am>而不是势能，Potential Energy = -<an|(1/r)|am>
function Probability = p(a,b)
Probability = (pi/(a+b))^(3/2);
end
function Potential = v(a,b)
Potential = -2*pi/(a+b);
end
function Motion = t(a,b)
Motion = 3*a*b*pi^(3/2)/((a+b)^(5/2));
end



