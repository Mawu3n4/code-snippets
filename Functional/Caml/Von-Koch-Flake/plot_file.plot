set term png;
set output "fichier.png";
set xrange [-200:200];
set yrange [-200:200];
plot "plot_data.txt" using 1:2 with lines;
