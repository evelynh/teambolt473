close all;
%{
CSV formated s.t. each row corresponds to a trial
i.e. row 1 = trial 0
col 1 = wolf, col2 = sheep
%}

%Load in CSVs
ws_pairs = csvread('CSVs_v2/generated/ws_pairs.csv');
s0 = csvread('CSVs_v2/generated/Sphero0_p2m_points.csv');
s1 = csvread('CSVs_v2/generated/Sphero1_p2m_points.csv');
s2 = csvread('CSVs_v2/generated/Sphero2_p2m_points.csv');
s3 = csvread('CSVs_v2/generated/Sphero3_p2m_points.csv');
s4 = csvread('CSVs_v2/generated/Sphero4_p2m_points.csv');

%toGraph = [1, 4, 7, 14, 21, 24, 25, 26, 34];
toGraph = [4, 7, 14, 21, 24, 25, 34];

for i = 1:length(toGraph)
    figure(i);
    trial = toGraph(i);
    angle = corr_angle(trial);
    % disp(angle)
    % disp(trial)
    wolf = ws_pairs(trial+1,1);
    % disp('Wolf')
    % disp(wolf)
    subplot(1, 2, 1);
    hold on;
    %trial-1 because Matlab & CSV are 1 indexed, Python is 0 indexed
    filename = strcat('CSVs_v2/', 'Sphero', num2str(wolf), 'Trial', num2str(trial), '.csv');
    % disp(filename)
    WolfData = csvread(filename);
    scatter(WolfData(:,2), WolfData(:,3), 'g');
    %Get the generated points for trial for Sphero
    %trial 0 in 1 and 2, trial 1 in 3 and 4, trial 2 in 4 and 5
    if wolf == 0
        gen_x = s0(trial*2+1,:);
        gen_y = s0(trial*2+2,:);
    elseif wolf == 1
        gen_x = s1(trial*2+1,:);
        gen_y = s1(trial*2+2,:);
    elseif wolf == 2
        gen_x = s2(trial*2+1,:);
        gen_y = s2(trial*2+2,:);
    elseif wolf == 3
        gen_x = s3(trial*2+1,:);
        gen_y = s3(trial*2+2,:);
    elseif wolf == 4
        gen_x = s4(trial*2+1,:);
        gen_y = s4(trial*2+2,:);
    end
    plot(gen_x, gen_y, 'b');
    sp_w_title = strcat('Wolf, Trial ', num2str(trial), ' Angle=', num2str(angle)); 
    title(sp_w_title)
    legend('Generated', 'Actual');

    sheep = ws_pairs(trial+1,2);
    % disp(sheep)
    subplot(1, 2, 2);
    hold on;
    filename = strcat('CSVs_v2/Sphero', num2str(sheep), 'Trial', num2str(trial), '.csv');
    % disp(filename)
    SheepData = csvread(filename);
    scatter(SheepData(:,2), SheepData(:,3), 'g');
    if sheep == 0
        gen_x = s0(trial*2+1,:);
        gen_y = s0(trial*2+2,:);
    elseif sheep == 1
        gen_x = s1(trial*2+1,:);
        gen_y = s1(trial*2+2,:);
    elseif sheep == 2
        gen_x = s2(trial*2+1,:);
        gen_y = s2(trial*2+2,:);
    elseif sheep == 3
        gen_x = s3(trial*2+1,:);
        gen_y = s3(trial*2+2,:);
    elseif sheep == 4
        gen_x = s4(trial*2+1,:);
        gen_y = s4(trial*2+2,:);
    end
    plot(gen_x, gen_y, 'b');
    sp_s_title = strcat('Sheep, Trial ', num2str(trial), ', Angle=', num2str(angle));
    title(sp_s_title)
    legend('Generated', 'Actual');
    hold off;
    saved_file = strcat('Trial', num2str(trial));
    print(saved_file,'-dpng' );
end