
# Sharing is Caring

## Challenge
* Category: Forensics
* Points: 250


Hey Challanger. I know you're putting together that Veteran's Day presentation. Here's all the U.S. service seals straight from Wikipedia. I think you'll only need four of them to get the points across. More than that is just excessive, but it's up to you.


### Hints
* Research split secret schemes
* Four out of five secrets are required
* Additional Hint: (Sharing is Caring) Our code uses a publically available implementation posted in a very visible location on the Internet. Not all implementations are interoperable.


## Solution

### Tools
* [exiftool](https://exiftool.org/)
* [strings](https://linux.die.net/man/1/strings)
* [secret-sharing](https://github.com/blockstack/secret-sharing)

This challenge is no longer available, but we should be able to recreate it from my notes and the files.tgz.


Lets start by opening our archive. It extracts 4  png files in images directory
```
$ tar xzvf files.tgz
```

Run strings against the four #.png files ie: `$ strings 1.png`. Im truncating the output to just the interesting parts:


```
1.png
1-9608474170977308238036624146101441469538628637045706610338073590812843162969037926492967854559828114435865261425719619743472419864336210874222029453059741

3.png
3-224183841656780872927678242626279871433733831057475254917387185998520511272846647279913467443558309288829498488402883425874249712684215384203475752039681175

5.png
5-1015950427545472565825761297620151258974491880324557727968398393745824130327315926142371765654543965113857776728721730398986530543452098367721676829359089545
```


Ok. so 2.png and 4.png did not return any info like above. So lets examine them with `$ exiftool 2.png`. Instructions for installing exiftool are available [here]('https://linoxide.com/linux-how-to/install-use-exiftool-linux-ubuntu-centos/'). Im truncating the output to just the interesting parts:

```
$ exiftool 2.png
Artist: 2-68500755079349789351078524541708453870296292990294021018027228505078681492284299873863659247273461856762128786874833326789786067325816477066780304059822843

$ exiftool 4.png
Artist: 4-524164732834933988556388319839274528391312080836319720002737667326861328789556912063222725295339950383555529443266354316704089242529615243887408038702736241
```

Ok. in researching split secret schemes, I found that a secret is split by a number of physically separated shares. Looks like that is what we found above. So lets see what programs can conduct the reverse.

This program [secret-sharing](https://github.com/blockstack/secret-sharing) on github reverses int LONG back into the secret. We are interested in the `points_to_secret_int()` function since we have long int's.

Install the github repo. Note, it is strictly python2.
```
$ pip install secretsharing
```
The program function `points_to_secret_int()` will return a secret as an intL. So Use my script that will it to a printable flag
```
$ python score.py
Secret INT: 29519221060413491828088933152834799057905028082883709692274022701262909290365
Flag: ACI{57937d9841a0e8a94e579af8617}
```

**ACI{57937d9841a0e8a94e579af8617}**
