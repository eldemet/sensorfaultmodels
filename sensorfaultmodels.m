%% Sensor fault models based on Reppa et al. 2016

clear
y0 = 10*ones(1,100)% %+ 0.5* sin(1:100);
figure
plot(y0)
hold on

events.t1{1} = 2 % time step start
events.t2{1} = 10 % time step end
events.a1{1} = 0.5 % parameter in occurance evolution profile function
events.a2{1} = 0.7 % parameter in dissapearance evolution profile function
events.functiontype{1} = 'constant'; 
events.functionpar{1} = 3  %constant difference

events.t1{2} = 20 % time step start
events.t2{2} = 30 % time step end
events.a1{2} = 999999 % parameter in occurance evolution profile function
events.a2{2} = 1 % parameter in dissapearance evolution profile function
events.functiontype{2} = 'drift'; 
events.functionpar{2} = 1  %constant difference

events.t1{3} = 40 % time step start
events.t2{3} = 50 % time step end
events.a1{3} = 100 % parameter in occurance evolution profile function
events.a2{3} = 100 % parameter in dissapearance evolution profile function
events.functiontype{3} = 'normal'; 
events.functionpar{3} = 2  %constant difference

events.t1{4} = 70 % time step start
events.t2{4} = inf % time step end
events.a1{4} = 999999 % parameter in occurance evolution profile function
events.a2{4} = 0.7 % parameter in dissapearance evolution profile function
events.functiontype{4} = 'constant'; 
events.functionpar{4} = -2  %constant difference

n = length(events.t1);

df = zeros(length(y0));
beta = zeros(length(y0));
f = zeros(length(y0));

for k = 1:length(y0)
    y0k = y0(k);
    for i = 1 : n
        T1 = events.t1{i};
        T2 = events.t2{i};
        a1 = events.a1{i};
        a2 = events.a2{i};
        ftype = events.functiontype{i};
        fpar = events.functionpar{i};
        
        b1 = 0;
        b2 = 0;
        if k >= T1   
            b1 = 1 - exp(- a1 * (k-T1));
        end
        if k >= T2 
            b2 = 1 - exp(- a2 * (k-T2));
        end
         
        b = b1 - b2;
        
        phi = 0;
        
        if b > 0 
            if strcmp(ftype,'constant') 
                phi = fpar;
            end
            if strcmp(ftype,'drift') 
                phi = fpar * (k - T1);
            end
            if strcmp(ftype,'normal') 
                phi = normrnd(0,fpar);
            end
        end
        
        df = b * phi;
        
        y0k = y0k + df;
    end
    y(k) = y0k;
end

plot(y)

grid on
