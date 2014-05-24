
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

let dragon n = Printf.printf "%d\n" n;;

let argv = Sys.argv;;

if (Array.length argv) != 2
then print_endline "Usage: ./dragon [n]"
else dragon (int_of_string argv.(1));;
