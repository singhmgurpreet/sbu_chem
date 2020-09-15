tiledlayout(3,1)
nexttile
plot(GS_211_134G_NVO_60(:,1),GS_211_134G_NVO_60(:,2),'k')
title('NVO 60');
xlim([0 400])
nexttile
plot(GS_211_134D_NVO_80(:,1),GS_211_134D_NVO_80(:,2),'r')
title('NVO 80');
xlim([0 400])
nexttile
plot(GS_211_134F_NVO_100(:,1),GS_211_134F_NVO_100(:,2),'b')
xlim([0 400])