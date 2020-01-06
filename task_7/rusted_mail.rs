extern crate regex;
use regex::Regex;
use std::io;

fn main() {
    let mut line = String::new();



    println!("Enter your email id :");
    let mut b1:String=io::stdin().read_line(&mut line).unwrap().to_string();
    let sa: Regex = Regex::new(r"^[A-Za-z0-9!#$%&'*+=?^_`{|}~.]+@[a-zA-z0-9]+\.[a-z]*").unwrap();
    let w=sa.is_match( &mut line);
    if w{
        println!("valid")
        }
    else{

        println!("invalid")
        }
}

