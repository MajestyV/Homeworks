clc;
clear all;
close all;

t = 2.5;
n = 1000;
dim = 2; 
G = [0,0];
M = [1/2,1/2];
K = [2/3,1/3];
eigval_new = zeros(dim,1);
wavenumbers = zeros(dim,n+1);
Dk = zeros(dim,dim);

count = 1;

%%
k1v = linspace(G(1),M(1),n+1);
k2v = linspace(G(2),M(2),n+1);

for i = 1:n+1
    k1 = k1v(i);
    k2 = k2v(i);
    
    Dk = [3*t -t*(1+exp(-1i*2*pi*k1)+exp(-1i*2*pi*k2));
          -t*(1+exp(1i*2*pi*k1)+exp(1i*2*pi*k2)) 3*t];
    
    eigval = eig(Dk);
    
    for j = 1:dim
 
    %Storing eigenvalue
    wavenumbers(j,count) = eigval(j);
       
%End of eigenvalue for-loop
    end
 
%Advancing counter
count = count+1;
 
%end of k value for-loop
end

%%
k1v = linspace(M(1),K(1),n+1);
k2v = linspace(M(2),K(2),n+1);

for i = 1:n+1
    k1 = k1v(i);
    k2 = k2v(i);
    
    Dk = [3*t -t*(1+exp(-1i*2*pi*k1)+exp(-1i*2*pi*k2));
          -t*(1+exp(1i*2*pi*k1)+exp(1i*2*pi*k2)) 3*t];
    
    eigval = eig(Dk);
    
    for j = 1:dim
 
    %Storing eigenvalue
    wavenumbers(j,count-1) = eigval(j);
       
%End of eigenvalue for-loop
    end
 
%Advancing counter
count = count+1;
 
%end of k value for-loop
end

%%
k1v = linspace(K(1),G(1),n+1);
k2v = linspace(K(2),G(2),n+1);

for i = 1:n+1
    k1 = k1v(i);
    k2 = k2v(i);
    
    Dk = [3*t -t*(1+exp(-1i*2*pi*k1)+exp(-1i*2*pi*k2));
          -t*(1+exp(1i*2*pi*k1)+exp(1i*2*pi*k2)) 3*t];
    
    eigval = eig(Dk);
    
    for j = 1:dim
 
    %Storing eigenvalue
    wavenumbers(j,count-2) = eigval(j);
       
%End of eigenvalue for-loop
    end
 
%Advancing counter
count = count+1;
 
%end of k value for-loop
end

%%
domain = linspace(0,1.5,3*n+1);
hold on
for p = 1:dim
    plot(domain,wavenumbers(p,:));
end
set(gca,'xticklabel',[]);
xlabel('\Gamma                                 M                                 K                                 \Gamma');
ylabel('Energy (eV)');