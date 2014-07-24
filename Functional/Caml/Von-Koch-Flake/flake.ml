let pi = 4. *. (atan 1.);;

type pen = {mutable d : float;
            mutable x : float;
            mutable y : float
};;

let new_pen() = {d = pi/.2.0; x = 0.0; y = 0.0};;

let ceil nb = if (nb < 0.0) then int_of_float(nb -. 0.5) else int_of_float(nb +. 0.5);;

let print_pos t = Printf.printf "%d %d\n" (ceil t.x) (ceil t.y);;

let move t dist = t.x <- t.x +. dist*.(cos t.d);
                         t.y <- t.y +. dist*.(sin t.d);
                         print_pos t;;

let right t angle = t.d <- t.d -. angle;;

let rad_of_deg angle = angle *. (pi /. 180.);;
let left t angle = t.d <- t.d +. (rad_of_deg angle);;

let pen = new_pen ();;

let rec cote n size_side =
  match n with
  | 0 -> move pen size_side
  | _ -> cote (n - 1) (size_side /. 3.); left pen 60.;
    cote (n - 1) (size_side /. 3.); left pen (-120.);
    cote (n - 1) (size_side /. 3.); left pen 60.;
    cote (n - 1) (size_side /. 3.);
;;

let flake n size_side =
  cote n size_side; left pen (-120.);
  cote n size_side; left pen (-120.);
  cote n size_side; left pen (-120.);;

let argv = Sys.argv;;

if (Array.length argv) != 3
|| (Array.length argv) = 3 && ((int_of_string argv.(2)) < 10 || (int_of_string argv.(2)) > 151)
then print_endline "Usage: ./flake [n] [10 <= size <= 150]"
else flake (int_of_string argv.(1)) (float_of_int(int_of_string argv.(2)));;
