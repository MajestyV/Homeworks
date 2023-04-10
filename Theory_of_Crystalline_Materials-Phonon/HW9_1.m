G1 = [0,0,0];
M = [1/2,0,0];
K = [1/2,1/2,0];
D = [1/2,1/2,1/2];
G2 = [1,1,1];

count = 1;

% Dispersion relation
% wk = sqrt(6+2*cos(2*pi*x)+2*cos(2*pi*y)+2*cos(2*pi*z))

n = 100;
x1v = linspace(G1(1),M(1),n+1);
x2v = linspace(M(2),K(2),n+1);
x3v = linspace(K(3),D(3),n+1);
x4v = linspace(D(1),G2(1),n+1);

% G1 to M
for i = 1:n+1
    x = x1v(i);
 wk = sqrt(6+2*cos(2*pi*x)+2+2);
end
count = count+1;

% M to K
for i = 1:n+1
    x = x2v(i);
 wk = sqrt(6-2+2*cos(2*pi*x)+2);
end

% K to D
for i = 1:n+1
    x = x3v(i);
 wk = sqrt(6-4+2*cos(2*pi*x));
end

% D to G2
for i = 1:n+1
    x = x4v(i);
 wk = sqrt(6+6*cos(2*pi*x)); 
end


plot(x,wk);
