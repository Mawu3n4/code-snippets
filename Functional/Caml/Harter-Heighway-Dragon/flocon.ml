let pi = 4. *. (atan 1.);;

type tortue = {mutable d : float;
               mutable x : float;
               mutable y : float
};;

let nouvelle_tortue() = {d = pi/.2.0; x = 0.0; y = 0.0};;

(* Arrondi le float a l'entier superieur *)
let ceil nb = if (nb < 0.0) then int_of_float(nb -. 0.5) else int_of_float(nb +. 0.5);;

(* ecrire position courrante sur sortie standard --> pour traitement gnuplot *)
let ecrire_position t = Printf.printf "%d %d\n" (ceil t.x) (ceil t.y);;

(* avancer la tortue t de distance *)
let avancer t distance = t.x <- t.x +. distance*.(cos t.d);
                         t.y <- t.y +. distance*.(sin t.d);
			 ecrire_position t;;

(* tourner la tortue de angle vers la droite *)
let droite t angle = t.d <- t.d -. angle;;

(* tourner la tortue de angle vers la gauche *)

let rad_of_deg angle = angle *. (pi /. 180.);;
let gauche t angle = t.d <- t.d +. (rad_of_deg angle);;

let franklin = nouvelle_tortue ();;

let rec cote n size_side =
  match n with
  | 0 -> avancer franklin size_side
  | _ -> cote (n - 1) (size_side /. 3.); gauche franklin 60.;
    cote (n - 1) (size_side /. 3.); gauche franklin (-120.);
    cote (n - 1) (size_side /. 3.); gauche franklin 60.;
    cote (n - 1) (size_side /. 3.);
;;

let flocon n size_side =
  cote n size_side; gauche franklin (-120.);
  cote n size_side; gauche franklin (-120.);
  cote n size_side; gauche franklin (-120.);;

let argv = Sys.argv;;

if (Array.length argv) != 3
|| (Array.length argv) = 3 && ((int_of_string argv.(2)) < 10 || (int_of_string argv.(2)) > 151)
then print_endline "Usage: ./flocon [n] [10 <= size <= 150]"
else flocon (int_of_string argv.(1)) (float_of_int(int_of_string argv.(2)));;

(* Question 5 & 6 - *)
(* Il est interessant de tester le programme avec n = 0 pour verifier    *)
(* l'affichage d'un triangle simple et n > 10 pour verifier l'efficacite *)
(* de la recursion et qu'il n'y pas de soucis de stack.			 *)
(*									 *)
(* NbCote = 4 * (n ^ 4) *)
(* Et il y a 3 appel recursif pour chaque valeurs de n superieure a zero. *)
(* Il y a donc en tout : (n - 1) * 3 appels recursif			  *)
