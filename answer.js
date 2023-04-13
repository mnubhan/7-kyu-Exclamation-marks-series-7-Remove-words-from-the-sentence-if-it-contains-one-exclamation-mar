function remove(s){
  return s.split(' ').filter(i => i.split('!').length != 2).join(' ');
}

const remove = $ => $.split(/\s+/).filter(el => !/^(!\w+|\w+!)$/.test(el)).join(" ")
