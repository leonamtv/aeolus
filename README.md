# ***a e o l u s***

```

                                                                                                     
         .8.          8 8888888888       ,o888888o.     8 8888         8 8888      88    d888888o.   
        .888.         8 8888          . 8888     `88.   8 8888         8 8888      88  .`8888:' `88. 
       :88888.        8 8888         ,8 8888       `8b  8 8888         8 8888      88  8.`8888.   Y8 
      . `88888.       8 8888         88 8888        `8b 8 8888         8 8888      88  `8.`8888.     
     .8. `88888.      8 888888888888 88 8888         88 8 8888         8 8888      88   `8.`8888.    
    .8`8. `88888.     8 8888         88 8888         88 8 8888         8 8888      88    `8.`8888.   
   .8' `8. `88888.    8 8888         88 8888        ,8P 8 8888         8 8888      88     `8.`8888.  
  .8'   `8. `88888.   8 8888         `8 8888       ,8P  8 8888         ` 8888     ,8P 8b   `8.`8888. 
 .888888888. `88888.  8 8888          ` 8888     ,88'   8 8888           8888   ,d8P  `8b.  ;8.`8888 
.8'       `8. `88888. 8 888888888888     `8888888P'     8 888888888888    `Y88888P'    `Y8888P ,88P' 

```

This project is a script that takes a term, matches it with a url defined in the json database in the resources folder and takes you to that url so you don't have to remember hundreds of urls.

## Usage

### As a standalone python program

#### To go to a url

```bash
python aeolus.py -m github -g
python aeolus.py --matcher github --go-to
```

#### To print the matched url

```bash
python aeolus.py -m github -p
python aeolus.py --matcher github --print-details
```

#### To add a url+term to match

```bash
python aeolus.py -t github -u www.github.com
python aeolus.py --add-term github --add-url www.github.com
```

### As a *bash* or *zsh* command

There are way more professional ways of doing this but the following instructions offer a beginner friendly way of using the script in **bash** or **zsh** (also works in **git bash**). 

For the script to work you need to make it available in the path. For that, you'll have to edit (or create, in case you have never done this before) a source file for your terminal of choice:

- If you use **bash** or **git bash** the file you'll have to edit/create a file called `.bashrc`
- If you use **zsh** the file you'll have to edit/create a file called `.zshrc`

In both cases, the source file should be at the home directory (type `cd ~` to get to it).

Add the following lines to the file:

```bash
aeolus_path="<path to the directory where you cloned this project>"

function aeolus() {
    pushd . >> /dev/null
    cd $aeolus_path
    python aeolus.py -m $1 -g | tail -n +1 >> /dev/null
    popd >> /dev/null
}

function aeolusa() {
    pushd . >> /dev/null
    cd $aeolus_path
    python aeolus.py $@ | tail -n +1 >> /dev/null
    popd >> /dev/null
}

function aeolusp() {
    pushd . >> /dev/null
    cd $aeolus_path
    python aeolus.py -m $1 -p | tail -n +1 >> /dev/null
    popd >> /dev/null
}
```