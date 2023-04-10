syms R2;
a = [13.0 1.96 0.44 0.12];
c = [0.0960 0.1637 0.1868 0.0719];

Ham = (v(a(1),a(1),0,0)+t(a(1),a(1),0,0)+v(a(1),a(1),R2,R2)+t(a(1),a(1),R2,R2))*a(1)^2+ ...
      (v(a(2),a(2),0,0)+t(a(2),a(2),0,0)+v(a(2),a(2),R2,R2)+t(a(2),a(2),R2,R2))*a(2)^2+ ...
      (v(a(3),a(3),0,0)+t(a(3),a(3),0,0)+v(a(3),a(3),R2,R2)+t(a(3),a(3),R2,R2))*a(3)^2+ ...
      (v(a(4),a(4),0,0)+t(a(4),a(4),0,0)+v(a(4),a(4),R2,R2)+t(a(4),a(4),R2,R2))*a(4)^2;
Ovl = (o(a(1),a(1),0,0)+o(a(1),a(1),R2,R2))*a(1)^2+(o(a(2),a(2),0,0)+o(a(2),a(2),R2,R2))*a(2)^2+ ...
      (o(a(3),a(3),0,0)+o(a(3),a(3),R2,R2))*a(3)^2+(o(a(4),a(4),0,0)+o(a(4),a(4),R2,R2))*a(4)^2;

display(Ham);
display(Ovl);


               
       
        









function ol = o(a,b,r1,r2)
ol = exp(-a*b*(r1-r2)^2/(a+b))*(pi/(a+b))^1.5;
end
function pe = v(a,b,r1,r2)
rp = (a*r1+b*r2)/(a+b);
pe = exp(-a*b*(r1-r2)^2/(a+b))*erf(sqrt((a+b)*(rp-r1)^2))*pi^1.5/((a+b)*sqrt((a+b)*(rp-r1)^2))+ ...
     exp(-a*b*(r1-r2)^2/(a+b))*erf(sqrt((a+b)*(rp-r2)^2))*pi^1.5/((a+b)*sqrt((a+b)*(rp-r2)^2))+ ...
     1/r2;
end
function ke = t(a,b,r1,r2)
ke = exp(-a*b*(r1-r2)^2/(a+b))*(a*b/(a+b))*(3-2*a*b*(r1-r2)^2/(a+b))*(pi/(a+b))^1.5;
end