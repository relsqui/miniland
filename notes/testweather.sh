#!/bin/bash

a() {
    DAYS=$(expr $RANDOM % 3 + 1 + 1)
    REMAINING=$(expr $1 - $DAYS)
    echo "cool and clear for $DAYS days"
    if [ $REMAINING -lt 0 ]; then exit 0; fi
    NEXT=$(expr $RANDOM % 100 + 1)
    if [ $NEXT -lt 10 ]; then
        echo "it warms up a little"
        k $REMAINING
    elif [ $NEXT -lt 25 ]; then
        echo "a light rain begins to fall"
        d $REMAINING
    else
        echo "clouds roll in and it starts to rain"
        b $REMAINING
    fi
}

b() {
    DAYS=$(expr $RANDOM % 3 + 1)
    REMAINING=$(expr $1 - $DAYS)
    echo "heavy rain for $DAYS days"
    if [ $REMAINING -lt 0 ]; then exit 0; fi
    NEXT=$(expr $RANDOM % 100 + 1)
    if [ $NEXT -lt 10 ]; then
        echo "the wind picks up"
        e $REMAINING
    elif [ $NEXT -lt 25 ]; then
        echo "the skies clear"
        k $REMAINING
    else
        echo "the skies clear"
        g $REMAINING
    fi
}

c() {
    DAYS=$(expr $RANDOM % 2 + 1)
    REMAINING=$(expr $1 - $DAYS)
    echo "windy with light rain for $DAYS days"
    if [ $REMAINING -lt 0 ]; then exit 0; fi
    NEXT=$(expr $RANDOM % 100 + 1)
    if [ $NEXT -lt 10 ]; then
        echo "the rain stops"
        f $REMAINING
    elif [ $NEXT -lt 50 ]; then
        echo "the rain stops, and the air grows cold"
        h $REMAINING
    else
        echo "it really starts coming down"
        e $REMAINING
    fi
}

d() {
    DAYS=$(expr $RANDOM % 2 + 1)
    REMAINING=$(expr $1 - $DAYS)
    echo "light rain for $DAYS days"
    if [ $REMAINING -lt 0 ]; then exit 0; fi
    NEXT=$(expr $RANDOM % 100 + 1)
    if [ $NEXT -lt 15 ]; then
        echo "the rain stops"
        k $REMAINING
    elif [ $NEXT -lt 50 ]; then
        echo "the wind picks up"
        c $REMAINING
    else
        echo "the wind picks up, blowing the rain away"
        f $REMAINING
    fi
}

e() {
    echo "windy and very rainy for 1 days"
    if [ $REMAINING -lt 0 ]; then exit 0; fi
    NEXT=$(expr $RANDOM % 100 + 1)
    if [ $NEXT -lt 15 ]; then
        echo "the sky clears"
        h $REMAINING
    else
        echo "the sky clears, and the wind dies down"
        g $REMAINING
    fi
}

f() {
    DAYS=$(expr $RANDOM % 3 + 1)
    REMAINING=$(expr $1 - $DAYS)
    echo "warm and windy for $DAYS days"
    if [ $REMAINING -lt 0 ]; then exit 0; fi
    NEXT=$(expr $RANDOM % 100 + 1)
    if [ $NEXT -lt 15 ]; then
        echo "the wind calms down a little"
        i $REMAINING
    else
        echo "the temperature drops"
        h $REMAINING
    fi
}

g() {
    DAYS=$(expr $RANDOM % 7 + 1)
    REMAINING=$(expr $1 - $DAYS)
    echo "cold and clear for $DAYS days"
    if [ $REMAINING -lt 0 ]; then exit 0; fi
    NEXT=$(expr $RANDOM % 100 + 1)
    if [ $NEXT -lt 10 ]; then
        echo "dark thunderheads roll in"
        j $REMAINING
    else
        k $REMAINING
    fi
}

h() {
    DAYS=$(expr $RANDOM % 2 + 1)
    REMAINING=$(expr $1 - $DAYS)
    echo "cold and windy for $DAYS days"
    if [ $REMAINING -lt 0 ]; then exit 0; fi
    NEXT=$(expr $RANDOM % 100 + 1)
    if [ $NEXT -lt 10 ]; then
        echo "the wind eases off"
        g $REMAINING
    elif [ $NEXT -lt 25 ]; then
        echo "the wind eases off, and it warms up"
        i $REMAINING
    else
        echo "dark thunderheads roll in"
        j $REMAINING
    fi
}

i() {
    DAYS=$(expr $RANDOM % 7 + 1)
    REMAINING=$(expr $1 - $DAYS)
    echo "warm and clear for $DAYS days"
    if [ $REMAINING -lt 0 ]; then exit 0; fi
    NEXT=$(expr $RANDOM % 100 + 1)
    if [ $NEXT -lt 10 ]; then
        echo "the temperature drops suddenly, and dark thunderheads roll in"
        j $REMAINING
    else
        k $REMAINING
    fi
}

j() {
    DAYS=$(expr $RANDOM % 3 + 1)
    REMAINING=$(expr $1 - $DAYS)
    echo "thunderstorms for $DAYS days"
    if [ $REMAINING -lt 0 ]; then exit 0; fi
    NEXT=$(expr $RANDOM % 100 + 1)
    if [ $NEXT -lt 10 ]; then
        echo "the storm dies down"
        g $REMAINING
    elif [ $NEXT -lt 55 ]; then
        echo "the rain stops, leaving its warm cloud clover behind"
        i $REMAINING
    else
        echo "the storm passes"
        k $REMAINING
    fi
}

k() {
    DAYS=$(expr $RANDOM % 7 + 1)
    REMAINING=$(expr $1 - $DAYS)
    echo "mild and calm for $DAYS days"
    if [ $REMAINING -lt 0 ]; then exit 0; fi
    NEXT=$(expr $RANDOM % 100 + 1)
    if [ $NEXT -lt 33 ]; then
        a $REMAINING
    elif [ $NEXT -lt 66 ]; then
        i $REMAINING
    else
        g $REMAINING
    fi
}

k 28
