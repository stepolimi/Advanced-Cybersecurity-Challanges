# JHON

- objdump -dj .text john > john.txt  to get the dissambled code
- identify pacing and unpacing routines
- gdb ./john
- b *0x804928a
- run c     	--> this 2 commands are to run the depacker code section
- dump binary memory result.bin 0x8048000 0x804cfff    --> to have the depacked binary
- import it to ghidra as raw binary, 32 bit, x86, gcc   (main start at 0x804970e -->)

flag{packer-4a3-1337&-annoying__}

b *0x804928a
run flag{packer-4a3-1337aaaaaaaaaaaa}
c
c
c ->sembra giusto
--start "packer"
c
c
c
c
c
c
c
c
--end "packer"
si --> call eax

eax -> strlen(flag)


https://ctftime.org/writeup/1496
https://ctftime.org/writeup/1504


dump binary memory result8.bin 0x8048000 0x804cfff

--check c4/c5--

b *0x80496ed
run flag{paaaaaaaaaaaaaaaaaaaaaaaaaa}

--checkc6-c7
b *0x804928a
run "flag{packer-4a3-1337&aaaaaaaaaaa}"
c
c
c
c
c
c
c
c
c
c
c
c
si
b *0x804951d
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c



--check c8
b *0x804928a
run "flag{packer-4a3-1337&-annoying__}"
c
c
c
c
c
c
c
c
c
c
c
c
si
b *0x804951d
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
si
b *0x80495ad
c
c
c
c
c
c
c
c
c
c
c
c
c

c8
recursive call: 0x80495d7

c*12 -> 1* check



john:     file format elf32-i386


Disassembly of section .text:

080490d0 <.text>:
 80490d0:	31 ed                	xor    %ebp,%ebp
 80490d2:	5e                   	pop    %esi
 80490d3:	89 e1                	mov    %esp,%ecx
 80490d5:	83 e4 f0             	and    $0xfffffff0,%esp
 80490d8:	50                   	push   %eax
 80490d9:	54                   	push   %esp
 80490da:	52                   	push   %edx
 80490db:	e8 23 00 00 00       	call   8049103 <powl@plt+0x43>
 80490e0:	81 c3 20 2f 00 00    	add    $0x2f20,%ebx
 80490e6:	8d 83 00 d9 ff ff    	lea    -0x2700(%ebx),%eax
 80490ec:	50                   	push   %eax
 80490ed:	8d 83 a0 d8 ff ff    	lea    -0x2760(%ebx),%eax
 80490f3:	50                   	push   %eax
 80490f4:	51                   	push   %ecx
 80490f5:	56                   	push   %esi
 80490f6:	c7 c0 5b 98 04 08    	mov    $0x804985b,%eax
 80490fc:	50                   	push   %eax
 80490fd:	e8 9e ff ff ff       	call   80490a0 <__libc_start_main@plt>
 8049102:	f4                   	hlt    
 8049103:	8b 1c 24             	mov    (%esp),%ebx
 8049106:	c3                   	ret    
 8049107:	66 90                	xchg   %ax,%ax
 8049109:	66 90                	xchg   %ax,%ax
 804910b:	66 90                	xchg   %ax,%ax
 804910d:	66 90                	xchg   %ax,%ax
 804910f:	90                   	nop
 8049110:	c3                   	ret    
 8049111:	66 90                	xchg   %ax,%ax
 8049113:	66 90                	xchg   %ax,%ax
 8049115:	66 90                	xchg   %ax,%ax
 8049117:	66 90                	xchg   %ax,%ax
 8049119:	66 90                	xchg   %ax,%ax
 804911b:	66 90                	xchg   %ax,%ax
 804911d:	66 90                	xchg   %ax,%ax
 804911f:	90                   	nop
 8049120:	8b 1c 24             	mov    (%esp),%ebx
 8049123:	c3                   	ret    
 8049124:	66 90                	xchg   %ax,%ax
 8049126:	66 90                	xchg   %ax,%ax
 8049128:	66 90                	xchg   %ax,%ax
 804912a:	66 90                	xchg   %ax,%ax
 804912c:	66 90                	xchg   %ax,%ax
 804912e:	66 90                	xchg   %ax,%ax
 8049130:	b8 50 c0 04 08       	mov    $0x804c050,%eax
 8049135:	3d 50 c0 04 08       	cmp    $0x804c050,%eax
 804913a:	74 24                	je     8049160 <powl@plt+0xa0>
 804913c:	8b 05 f4 bf 04 08    	mov    0x804bff4,%eax
 8049142:	85 c0                	test   %eax,%eax
 8049144:	74 1a                	je     8049160 <powl@plt+0xa0>
 8049146:	55                   	push   %ebp
 8049147:	89 e5                	mov    %esp,%ebp
 8049149:	83 ec 14             	sub    $0x14,%esp
 804914c:	68 50 c0 04 08       	push   $0x804c050
 8049151:	ff d0                	call   *%eax
 8049153:	83 c4 10             	add    $0x10,%esp
 8049156:	c9                   	leave  
 8049157:	c3                   	ret    
 8049158:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi
 804915f:	90                   	nop
 8049160:	c3                   	ret    
 8049161:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi
 8049168:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi
 804916f:	90                   	nop
 8049170:	b8 50 c0 04 08       	mov    $0x804c050,%eax
 8049175:	2d 50 c0 04 08       	sub    $0x804c050,%eax
 804917a:	c1 f8 02             	sar    $0x2,%eax
 804917d:	89 c2                	mov    %eax,%edx
 804917f:	c1 ea 1f             	shr    $0x1f,%edx
 8049182:	01 d0                	add    %edx,%eax
 8049184:	d1 f8                	sar    %eax
 8049186:	74 20                	je     80491a8 <powl@plt+0xe8>
 8049188:	8b 15 fc bf 04 08    	mov    0x804bffc,%edx
 804918e:	85 d2                	test   %edx,%edx
 8049190:	74 16                	je     80491a8 <powl@plt+0xe8>
 8049192:	55                   	push   %ebp
 8049193:	89 e5                	mov    %esp,%ebp
 8049195:	83 ec 10             	sub    $0x10,%esp
 8049198:	50                   	push   %eax
 8049199:	68 50 c0 04 08       	push   $0x804c050
 804919e:	ff d2                	call   *%edx
 80491a0:	83 c4 10             	add    $0x10,%esp
 80491a3:	c9                   	leave  
 80491a4:	c3                   	ret    
 80491a5:	8d 76 00             	lea    0x0(%esi),%esi
 80491a8:	c3                   	ret    
 80491a9:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi
 80491b0:	f3 0f 1e fb          	endbr32 
 80491b4:	80 3d 50 c0 04 08 00 	cmpb   $0x0,0x804c050
 80491bb:	75 1b                	jne    80491d8 <powl@plt+0x118>
 80491bd:	55                   	push   %ebp
 80491be:	89 e5                	mov    %esp,%ebp
 80491c0:	83 ec 08             	sub    $0x8,%esp
 80491c3:	e8 68 ff ff ff       	call   8049130 <powl@plt+0x70>
 80491c8:	c6 05 50 c0 04 08 01 	movb   $0x1,0x804c050
 80491cf:	c9                   	leave  
 80491d0:	c3                   	ret    
 80491d1:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi
 80491d8:	c3                   	ret    
 80491d9:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi
 80491e0:	f3 0f 1e fb          	endbr32 
 80491e4:	eb 8a                	jmp    8049170 <powl@plt+0xb0>
 80491e6:	55                   	push   %ebp
 80491e7:	89 e5                	mov    %esp,%ebp
 80491e9:	53                   	push   %ebx
 80491ea:	50                   	push   %eax
 80491eb:	8b 4d 08             	mov    0x8(%ebp),%ecx
 80491ee:	ba 67 66 66 66       	mov    $0x66666667,%edx
 80491f3:	89 c8                	mov    %ecx,%eax
 80491f5:	f7 ea                	imul   %edx
 80491f7:	d1 fa                	sar    %edx
 80491f9:	89 c8                	mov    %ecx,%eax
 80491fb:	c1 f8 1f             	sar    $0x1f,%eax
 80491fe:	29 c2                	sub    %eax,%edx
 8049200:	89 d0                	mov    %edx,%eax
 8049202:	89 c2                	mov    %eax,%edx
 8049204:	c1 e2 02             	shl    $0x2,%edx
 8049207:	01 c2                	add    %eax,%edx
 8049209:	89 c8                	mov    %ecx,%eax
 804920b:	29 d0                	sub    %edx,%eax
 804920d:	8b 14 85 3c c0 04 08 	mov    0x804c03c(,%eax,4),%edx
 8049214:	8b 45 08             	mov    0x8(%ebp),%eax
 8049217:	8b 4d 0c             	mov    0xc(%ebp),%ecx
 804921a:	89 c3                	mov    %eax,%ebx
 804921c:	8b 12                	mov    (%edx),%edx

 pack

 804921e:	31 13                	xor    %edx,(%ebx)
 8049220:	83 c3 04             	add    $0x4,%ebx
 8049223:	49                   	dec    %ecx
 8049224:	75 f8                	jne    804921e <powl@plt+0x15e>
 8049226:	58                   	pop    %eax

 8049227:	90                   	nop
 8049228:	5b                   	pop    %ebx
 8049229:	5d                   	pop    %ebp
 804922a:	c3                   	ret    
 804922b:	55                   	push   %ebp
 804922c:	89 e5                	mov    %esp,%ebp
 804922e:	83 ec 08             	sub    $0x8,%esp
 8049231:	8b 45 08             	mov    0x8(%ebp),%eax
 8049234:	25 00 f0 ff ff       	and    $0xfffff000,%eax
 8049239:	83 ec 04             	sub    $0x4,%esp
 804923c:	6a 07                	push   $0x7
 804923e:	68 00 10 00 00       	push   $0x1000
 8049243:	50                   	push   %eax
 8049244:	e8 f7 fd ff ff       	call   8049040 <mprotect@plt>
 8049249:	83 c4 10             	add    $0x10,%esp
 804924c:	8b 4d 08             	mov    0x8(%ebp),%ecx
 804924f:	ba 67 66 66 66       	mov    $0x66666667,%edx
 8049254:	89 c8                	mov    %ecx,%eax
 8049256:	f7 ea                	imul   %edx
 8049258:	d1 fa                	sar    %edx
 804925a:	89 c8                	mov    %ecx,%eax
 804925c:	c1 f8 1f             	sar    $0x1f,%eax
 804925f:	29 c2                	sub    %eax,%edx
 8049261:	89 d0                	mov    %edx,%eax
 8049263:	89 c2                	mov    %eax,%edx
 8049265:	c1 e2 02             	shl    $0x2,%edx
 8049268:	01 c2                	add    %eax,%edx
 804926a:	89 c8                	mov    %ecx,%eax
 804926c:	29 d0                	sub    %edx,%eax
 804926e:	8b 14 85 3c c0 04 08 	mov    0x804c03c(,%eax,4),%edx
 8049275:	8b 45 08             	mov    0x8(%ebp),%eax
 8049278:	8b 4d 0c             	mov    0xc(%ebp),%ecx
 804927b:	83 c4 08             	add    $0x8,%esp
 804927e:	50                   	push   %eax
 804927f:	8b 12                	mov    (%edx),%edx

 unpack

 8049281:	31 10                	xor    %edx,(%eax)
 8049283:	83 c0 04             	add    $0x4,%eax
 8049286:	49                   	dec    %ecx
 8049287:	75 f8                	jne    8049281 <powl@plt+0x1c1>
 8049289:	58                   	pop    %eax
 804928a:	ff d0                	call   *%eax

 804928c:	83 ec 08             	sub    $0x8,%esp
 804928f:	ff 75 0c             	pushl  0xc(%ebp)
 8049292:	ff 75 08             	pushl  0x8(%ebp)
 8049295:	e8 4c ff ff ff       	call   80491e6 <powl@plt+0x126>
 804929a:	83 c4 10             	add    $0x10,%esp
 804929d:	90                   	nop
 804929e:	c9                   	leave  
 804929f:	c3                   	ret    
 80492a0:	11 cc                	adc    %ecx,%esp
 80492a2:	a4                   	movsb  %ds:(%esi),%es:(%edi)
 80492a3:	c7                   	(bad)  
 80492a4:	a8 5d                	test   $0x5d,%al
 80492a6:	c2 a8 4c             	ret    $0x4ca8
 80492a9:	2d 78 e4 40 4d       	sub    $0x4d40e478,%eax
 80492ae:	be 31 5c ad 3b       	mov    $0x3bad5c31,%esi
 80492b3:	b9 bb ba c2 80       	mov    $0x80c2babb,%ecx
 80492b8:	54                   	push   %esp
 80492b9:	cc                   	int3   
 80492ba:	04 b0                	add    $0xb0,%al
 80492bc:	cf                   	iret   
 80492bd:	00 b5 7f 01 5d 34    	add    %dh,0x345d017f(%ebp)
 80492c3:	43                   	inc    %ebx
 80492c4:	fc                   	cld    
 80492c5:	44                   	inc    %esp
 80492c6:	41                   	inc    %ecx
 80492c7:	44                   	inc    %esp
 80492c8:	44                   	inc    %esp
 80492c9:	ae                   	scas   %es:(%edi),%al
 80492ca:	59                   	pop    %ecx
 80492cb:	c7                   	(bad)  
 80492cc:	a8 4d                	test   $0x4d,%al
 80492ce:	be 31 5c 2d 7e       	mov    $0x7e2d5c31,%esi
 80492d3:	e4 40                	in     $0x40,%al
 80492d5:	4d                   	dec    %ebp
 80492d6:	a9 31 b9 ba be       	test   $0xbebab931,%eax
 80492db:	c7 80 55 f9 44 44 45 	movl   $0xc38d4145,0x4444f955(%eax)
 80492e2:	41 8d c3 
 80492e5:	17                   	pop    %ss
 80492e6:	b9 d5 c1 ae 38       	mov    $0x38aec1d5,%ecx
 80492eb:	b3 ae                	mov    $0xae,%bl
 80492ed:	4e                   	dec    %esi
 80492ee:	cf                   	iret   
 80492ef:	45                   	inc    %ebp
 80492f0:	5a                   	pop    %edx
 80492f1:	aa                   	stos   %al,%es:(%edi)
 80492f2:	aa                   	stos   %al,%es:(%edi)
 80492f3:	cd bd                	int    $0xbd
 80492f5:	bd b3 f4 52 cf       	mov    $0xcf52f4b3,%ebp
 80492fa:	60                   	pusha  
 80492fb:	cf                   	iret   
 80492fc:	c9                   	leave  
 80492fd:	07                   	pop    %es
 80492fe:	28 31                	sub    %dh,(%ecx)
 8049300:	92                   	xchg   %eax,%edx
 8049301:	4d                   	dec    %ebp
 8049302:	86 30                	xchg   %dh,(%eax)
 8049304:	7e 3f                	jle    8049345 <powl@plt+0x285>
 8049306:	45                   	inc    %ebp
 8049307:	37                   	aaa    
 8049308:	fa                   	cli    
 8049309:	43                   	inc    %ebx
 804930a:	30 30                	xor    %dh,(%eax)
 804930c:	42                   	inc    %edx
 804930d:	a9 28 b3 ae 4a       	test   $0x4aaeb328,%eax
 8049312:	cf                   	iret   
 8049313:	45                   	inc    %ebp
 8049314:	5a                   	pop    %edx
 8049315:	2a 64 90 46          	sub    0x46(%eax,%edx,4),%ah
 8049319:	4a                   	dec    %edx
 804931a:	d8 01                	fadds  (%ecx)
 804931c:	bf bd cf b3 86       	mov    $0x86b3cfbd,%edi
 8049321:	52                   	push   %edx
 8049322:	88 30                	mov    %dh,(%eax)
 8049324:	42                   	inc    %edx
 8049325:	42                   	inc    %edx
 8049326:	30 f9                	xor    %bh,%cl
 8049328:	81 54 8b e6 87 ed 1a 	adcl   $0x801aed87,-0x1a(%ebx,%ecx,4)
 804932f:	80 
 8049330:	e8 0d fd 76 1c       	call   247b9042 <_IO_stdin_used@@Base+0x1c76f03e>
 8049335:	e9 54 fe fb fe       	jmp    700918e <strstr@plt-0x103fea2>
 804933a:	81 c7 14 88 47 f7    	add    $0xf7478814,%edi
 8049340:	c3                   	ret    
 8049341:	44                   	inc    %esp
 8049342:	f2 03 04 01          	repnz add (%ecx,%eax,1),%eax
 8049346:	02 e8                	add    %al,%ch
 8049348:	29 8a 57 f3 8f 44    	sub    %ecx,0x448ff357(%edx)
 804934e:	1a 02                	sbb    (%edx),%al
 8049350:	d4 0e                	aam    $0xe
 8049352:	b4 03                	mov    $0x3,%ah
 8049354:	80 c1 7b             	add    $0x7b,%cl
 8049357:	19 87 ed 0a fc 71    	sbb    %eax,0x71fc0aed(%edi)
 804935d:	19 6a 65             	sbb    %ebp,0x65(%edx)
 8049360:	a4                   	movsb  %ds:(%esi),%es:(%edi)
 8049361:	05 0a eb ec fd       	add    $0xfdeceb0a,%eax
 8049366:	fd                   	std    
 8049367:	fc                   	cld    
 8049368:	87 c5                	xchg   %eax,%ebp
 804936a:	12 bb 04 01 02 03    	adc    0x3020104(%ebx),%bh
 8049370:	ef                   	out    %eax,(%dx)
 8049371:	10 81 46 f4 00 89    	adc    %al,-0x76ff0bba(%ecx)
 8049377:	46                   	inc    %esi
 8049378:	f4                   	hlt    
 8049379:	3a 47 f7             	cmp    -0x9(%edi),%al
 804937c:	78 ca                	js     8049348 <powl@plt+0x288>
 804937e:	ba 02 04 01 02       	mov    $0x2010402,%edx
 8049383:	ca c7 17             	lret   $0x17c7
 8049386:	b9 d5 c1 ae 18       	mov    $0x18aec1d5,%ecx
 804938b:	eb 07                	jmp    8049394 <powl@plt+0x2d4>
 804938d:	5a                   	pop    %edx
 804938e:	ed                   	in     (%dx),%eax
 804938f:	35 12 e3 34 38       	xor    $0x3834e312,%eax
 8049394:	cf                   	iret   
 8049395:	26 14 c8             	es adc $0xc8,%al
 8049398:	9f                   	lahf   
 8049399:	5e                   	pop    %esi
 804939a:	14 bd                	adc    $0xbd,%al
 804939c:	26 66 c8 ed 5e 66    	es enterw $0x5eed,$0x66
 80493a2:	d8 89 be bd cf b3    	fmuls  -0x4c304242(%ecx)
 80493a8:	86 52 ed             	xchg   %dl,-0x13(%edx)
 80493ab:	35 1a e3 34 38       	xor    $0x3834e31a,%eax
 80493b0:	9c                   	pushf  
 80493b1:	8b ed                	mov    %ebp,%ebp
 80493b3:	6d                   	insl   (%dx),%es:(%edi)
 80493b4:	9a 99 75 28 9f 47 50 	lcall  $0x5047,$0x9f287599
 80493bb:	91                   	xchg   %eax,%ecx
 80493bc:	46                   	inc    %esi
 80493bd:	4a                   	dec    %edx
 80493be:	bd 54 66 ba ed       	mov    $0xedba6654,%ebp
 80493c3:	2c 66                	sub    $0x66,%al
 80493c5:	cf                   	iret   
 80493c6:	54                   	push   %esp
 80493c7:	14 ba                	adc    $0xba,%al
 80493c9:	9f                   	lahf   
 80493ca:	2c 14                	sub    $0x14,%al
 80493cc:	aa                   	stos   %al,%es:(%edi)
 80493cd:	cd cc                	int    $0xcc
 80493cf:	cf                   	iret   
 80493d0:	bd c1 f4 20 9f       	mov    $0x9f20f4c1,%ebp
 80493d5:	47                   	inc    %edi
 80493d6:	58                   	pop    %eax
 80493d7:	91                   	xchg   %eax,%ecx
 80493d8:	46                   	inc    %esi
 80493d9:	4a                   	dec    %edx
 80493da:	ee                   	out    %al,(%dx)
 80493db:	f9                   	stc    
 80493dc:	9e                   	sahf   
 80493dd:	2f                   	das    
 80493de:	e8 ed 1f 9a eb       	call   f39eb3d0 <_IO_stdin_used@@Base+0xeb9a13cc>
 80493e3:	75 5a                	jne    804943f <powl@plt+0x37f>
 80493e5:	9f                   	lahf   
 80493e6:	35 40 e3 46 38       	xor    $0x3846e340,%eax
 80493eb:	bd 26 66 c8 ed       	mov    $0xedc86626,%ebp
 80493f0:	5e                   	pop    %esi
 80493f1:	66 bd 54 66          	mov    $0x6654,%bp
 80493f5:	ba ed 2c 66 aa       	mov    $0xaa662ced,%edx
 80493fa:	52                   	push   %edx
 80493fb:	cc                   	int3   
 80493fc:	bd bd b3 f4 52       	mov    $0x52f4b3bd,%ebp
 8049401:	9f                   	lahf   
 8049402:	35 48 e3 46 38       	xor    $0x3846e348,%eax
 8049407:	ee                   	out    %al,(%dx)
 8049408:	8b 9e 75 e8 9f 1f    	mov    0x1f9fe875(%esi),%ebx
 804940e:	e8 eb 07 5a ed       	call   f55e9bfe <_IO_stdin_used@@Base+0xed59fbfa>
 8049413:	35 c2 e3 34 38       	xor    $0x3834e3c2,%eax
 8049418:	cf                   	iret   
 8049419:	26 14 c8             	es adc $0xc8,%al
 804941c:	9f                   	lahf   
 804941d:	5e                   	pop    %esi
 804941e:	14 bd                	adc    $0xbd,%al
 8049420:	26 66 c8 ed 5e 66    	es enterw $0x5eed,$0x66
 8049426:	d8 05 be bd cf b3    	fadds  0xb3cfbdbe
 804942c:	86 52 ed             	xchg   %dl,-0x13(%edx)
 804942f:	35 ca e3 34 38       	xor    $0x3834e3ca,%eax
 8049434:	9c                   	pushf  
 8049435:	8b ed                	mov    %ebp,%ebp
 8049437:	75 9a                	jne    80493d3 <powl@plt+0x313>
 8049439:	9c                   	pushf  
 804943a:	d1 eb                	shr    %ebx
 804943c:	07                   	pop    %es
 804943d:	5a                   	pop    %edx
 804943e:	ed                   	in     (%dx),%eax
 804943f:	35 d2 e3 34 38       	xor    $0x3834e3d2,%eax
 8049444:	9c                   	pushf  
 8049445:	8b ee                	mov    %esi,%ebp
 8049447:	f1                   	icebp  
 8049448:	9f                   	lahf   
 8049449:	47                   	inc    %edi
 804944a:	a8 91                	test   $0x91,%al
 804944c:	46                   	inc    %esi
 804944d:	4a                   	dec    %edx
 804944e:	ee                   	out    %al,(%dx)
 804944f:	f1                   	icebp  
 8049450:	9b                   	fwait
 8049451:	1f                   	pop    %ds
 8049452:	c4 c3 4d 52          	(bad)  
 8049456:	75 c4                	jne    804941c <powl@plt+0x35c>
 8049458:	b1 4d                	mov    $0x4d,%cl
 804945a:	1c f0                	sbb    $0xf0,%al
 804945c:	8b c3                	mov    %ebx,%eax
 804945e:	aa                   	stos   %al,%es:(%edi)
 804945f:	76 1a                	jbe    804947b <powl@plt+0x3bb>
 8049461:	7c 13                	jl     8049476 <powl@plt+0x3b6>
 8049463:	c7                   	(bad)  
 8049464:	74 ba                	je     8049420 <powl@plt+0x360>
 8049466:	e3 76                	jecxz  80494de <powl@plt+0x41e>
 8049468:	ba 1f 74 ba df       	mov    $0xdfba741f,%edx
 804946d:	76 ba                	jbe    8049429 <powl@plt+0x369>
 804946f:	1b 24 ba             	sbb    (%edx,%edi,4),%esp
 8049472:	e7 7c                	out    %eax,$0x7c
 8049474:	13 f7                	adc    %edi,%esi
 8049476:	72 9b                	jb     8049413 <powl@plt+0x353>
 8049478:	db 07                	fildl  (%edi)
 804947a:	22 e3                	and    %bl,%ah
 804947c:	db 17                	fistl  (%edi)
 804947e:	d1 03                	roll   (%ebx)
 8049480:	00 00                	add    %al,(%eax)
 8049482:	7c 3b                	jl     80494bf <powl@plt+0x3ff>
 8049484:	ef                   	out    %eax,(%dx)
 8049485:	24 ba                	and    $0xba,%al
 8049487:	e7 26                	out    %eax,$0x26
 8049489:	36 7c 13             	ss jl  804949f <powl@plt+0x3df>
 804948c:	f7 72 9b             	divl   -0x65(%edx)
 804948f:	db 0b                	fisttpl (%ebx)
 8049491:	24 c3                	and    $0xc3,%al
 8049493:	db 72 9b             	(bad)  -0x65(%edx)
 8049496:	db 0b                	fisttpl (%ebx)
 8049498:	24 c3                	and    $0xc3,%al
 804949a:	db 17                	fistl  (%edi)
 804949c:	df 03                	filds  (%ebx)
 804949e:	00 00                	add    %al,(%eax)
 80494a0:	7c 3b                	jl     80494dd <powl@plt+0x41d>
 80494a2:	df 24 d2             	fbld   (%edx,%edx,8)
 80494a5:	5f                   	pop    %edi
 80494a6:	5e                   	pop    %esi
 80494a7:	fb                   	sti    
 80494a8:	f7 26                	mull   (%esi)
 80494aa:	36 24 0e             	ss and $0xe,%al
 80494ad:	22 26                	and    (%esi),%ah
 80494af:	8c e0                	mov    %fs,%eax
 80494b1:	26 82 21 f0          	andb   $0xf0,%es:(%ecx)
 80494b5:	48                   	dec    %eax
 80494b6:	ba 21 7f 33 f3       	mov    $0xf3337f21,%edx
 80494bb:	99                   	cltd   
 80494bc:	76 ba                	jbe    8049478 <powl@plt+0x3b8>
 80494be:	23 26                	and    (%esi),%esp
 80494c0:	92                   	xchg   %eax,%edx
 80494c1:	23 20                	and    (%eax),%esp
 80494c3:	82 2f 26             	subb   $0x26,(%edi)
 80494c6:	92                   	xchg   %eax,%edx
 80494c7:	21 74 ba 2f          	and    %esi,0x2f(%edx,%edi,4)
 80494cb:	74 aa                	je     8049477 <powl@plt+0x3b7>
 80494cd:	2b 14 d4             	sub    (%esp,%edx,8),%edx
 80494d0:	24 d2                	and    $0xd2,%al
 80494d2:	5f                   	pop    %edi
 80494d3:	5e                   	pop    %esi
 80494d4:	fb                   	sti    
 80494d5:	f7 21                	mull   (%ecx)
 80494d7:	16                   	push   %ss
 80494d8:	26 82 21 f0          	andb   $0xf0,%es:(%ecx)
 80494dc:	48                   	dec    %eax
 80494dd:	ba 21 7f 33 f3       	mov    $0xf3337f21,%edx
 80494e2:	99                   	cltd   
 80494e3:	76 ba                	jbe    804949f <powl@plt+0x3df>
 80494e5:	23 26                	and    (%esi),%esp
 80494e7:	92                   	xchg   %eax,%edx
 80494e8:	23 20                	and    (%eax),%esp
 80494ea:	82 2f 26             	subb   $0x26,(%edi)
 80494ed:	92                   	xchg   %eax,%edx
 80494ee:	21 74 ba 2f          	and    %esi,0x2f(%edx,%edi,4)
 80494f2:	74 aa                	je     804949e <powl@plt+0x3de>
 80494f4:	2b 7e 0d             	sub    0xd(%esi),%edi
 80494f7:	ff                   	(bad)  
 80494f8:	ff                   	(bad)  
 80494f9:	ff                   	(bad)  
 80494fa:	7f 7c                	jg     8049578 <powl@plt+0x4b8>
 80494fc:	3f                   	aas    
 80494fd:	ea 7c 2d ff 76 ba 0f 	ljmp   $0xfba,$0x76ff2d7c
 8049504:	76 aa                	jbe    80494b0 <powl@plt+0x3f0>
 8049506:	0b 74 ba 0f          	or     0xf(%edx,%edi,4),%esi
 804950a:	74 aa                	je     80494b6 <powl@plt+0x3f6>
 804950c:	0b cc                	or     %esp,%ecx
 804950e:	ba 1f cc aa 1b       	mov    $0x1baacc1f,%edx
 8049513:	f6 2f                	imulb  (%edi)
 8049515:	7a 3f                	jp     8049556 <powl@plt+0x496>
 8049517:	f0 6b 3f f0          	lock imul $0xfffffff0,(%edi),%edi
 804951b:	49                   	dec    %ecx
 804951c:	3f                   	aas    
 804951d:	36 c3                	ss ret 
 804951f:	17                   	pop    %ss
 8049520:	b9 d5 c1 ae 38       	mov    $0x38aec1d5,%ecx
 8049525:	b3 ae                	mov    $0xae,%bl
 8049527:	4e                   	dec    %esi
 8049528:	cf                   	iret   
 8049529:	45                   	inc    %ebp
 804952a:	5a                   	pop    %edx
 804952b:	aa                   	stos   %al,%es:(%edi)
 804952c:	50                   	push   %eax
 804952d:	cb                   	lret   
 804952e:	bd bd b3 f4 52       	mov    $0x52f4b3bd,%ebp
 8049533:	c1 c8 11             	ror    $0x11,%eax
 8049536:	37                   	aaa    
 8049537:	45                   	inc    %ebp
 8049538:	88 31                	mov    %dh,(%ecx)
 804953a:	42                   	inc    %edx
 804953b:	42                   	inc    %edx
 804953c:	30 db                	xor    %bl,%bl
 804953e:	47                   	inc    %edi
 804953f:	fa                   	cli    
 8049540:	30 30                	xor    %dh,(%eax)
 8049542:	42                   	inc    %edx
 8049543:	00 c9                	add    %cl,%cl
 8049545:	c3                   	ret    
 8049546:	45                   	inc    %ebp
 8049547:	a9 d5 13 93 cc       	test   $0xcc9313d5,%eax
 804954c:	24 87                	and    $0x87,%al
 804954e:	55                   	push   %ebp
 804954f:	d4 b1                	aam    $0xb1
 8049551:	e0 14                	loopne 8049567 <powl@plt+0x4a7>
 8049553:	28 bb 05 0c a3 f0    	sub    %bh,-0xf5cf3fb(%ebx)
 8049559:	56                   	push   %esi
 804955a:	99                   	cltd   
 804955b:	e3 b3                	jecxz  8049510 <powl@plt+0x450>
 804955d:	ac                   	lods   %ds:(%esi),%al
 804955e:	1c df                	sbb    $0xdf,%al
 8049560:	45                   	inc    %ebp
 8049561:	58                   	pop    %eax
 8049562:	f8                   	clc    
 8049563:	09 cb                	or     %ecx,%ebx
 8049565:	bf ef a3 f4 50       	mov    $0x50f4a3ef,%edi
 804956a:	29 e3                	sub    %esp,%ebx
 804956c:	42                   	inc    %edx
 804956d:	47                   	inc    %edi
 804956e:	a8 21                	test   $0x21,%al
 8049570:	30 40 10             	xor    %al,0x10(%eax)
 8049573:	cb                   	lret   
 8049574:	5a                   	pop    %edx
 8049575:	cb                   	lret   
 8049576:	45                   	inc    %ebp
 8049577:	3c bb                	cmp    $0xbb,%al
 8049579:	05 e4 21 e0 4f       	add    $0x4fe021e4,%eax
 804957e:	a6                   	cmpsb  %es:(%edi),%ds:(%esi)
 804957f:	28 bb 05 0c ad 60    	sub    %bh,0x60ad0c05(%ebx)
 8049585:	54                   	push   %esp
 8049586:	9b                   	fwait
 8049587:	65 28 41 c0          	sub    %al,%gs:-0x40(%ecx)
 804958b:	2f                   	das    
 804958c:	86 40 21             	xchg   %al,0x21(%eax)
 804958f:	e8 b8 05 e2 ab       	call   b3e69b4c <_IO_stdin_used@@Base+0xabe1fb48>
 8049594:	75 5c                	jne    80495f2 <powl@plt+0x532>
 8049596:	93                   	xchg   %eax,%ebx
 8049597:	e0 25                	loopne 80495be <powl@plt+0x4fe>
 8049599:	c9                   	leave  
 804959a:	d2 ab 75 58 11 f0    	shrb   %cl,-0xfeea78b(%ebx)
 80495a0:	3f                   	aas    
 80495a1:	f6 10                	notb   (%eax)
 80495a3:	a8 75                	test   $0x75,%al
 80495a5:	b3 1f                	mov    $0x1f,%bl
 80495a7:	96                   	xchg   %eax,%esi
 80495a8:	75 b2                	jne    804955c <powl@plt+0x49c>
 80495aa:	2a 65 c3             	sub    -0x3d(%ebp),%ah
 80495ad:	34 17                	xor    $0x17,%al
 80495af:	98                   	cwtl   
 80495b0:	30 40 10             	xor    %al,0x10(%eax)
 80495b3:	20 db                	and    %bl,%bl
 80495b5:	69 9b 65 2c c3 d0 21 	imul   $0x18acb321,-0x2f3cd39b(%ebx),%ebx
 80495bc:	b3 ac 18 
 80495bf:	70 cf                	jo     8049590 <powl@plt+0x4d0>
 80495c1:	35 08 48 3b f0       	xor    $0xf03b4808,%eax
 80495c6:	bd fe 58 4b a0       	mov    $0xa04b58fe,%ebp
 80495cb:	8d                   	(bad)  
 80495cc:	ee                   	out    %al,(%dx)
 80495cd:	28 1b                	sub    %bl,(%ebx)
 80495cf:	90                   	nop
 80495d0:	9d                   	popf   
 80495d1:	9e                   	sahf   
 80495d2:	78 2b                	js     80495ff <powl@plt+0x53f>
 80495d4:	80 ed ce             	sub    $0xce,%ch
 80495d7:	c8 5a bf ef          	enter  $0xbf5a,$0xef
 80495db:	df b3 84 30 ab 6d    	fbstp  0x6dab3084(%ebx)
 80495e1:	bc c9 c3 aa 76       	mov    $0x76aac3c9,%esp
 80495e6:	1a a8 a9 ac 7e 13    	sbb    0x137eaca9(%eax),%ch
 80495ec:	73 ff                	jae    80495ed <powl@plt+0x52d>
 80495ee:	ff                   	(bad)  
 80495ef:	ff 74 ba e7          	pushl  -0x19(%edx,%edi,4)
 80495f3:	76 7a                	jbe    804966f <powl@plt+0x5af>
 80495f5:	8b 00                	mov    (%eax),%eax
 80495f7:	00 00                	add    %al,(%eax)
 80495f9:	9a 5e eb ff ff ff 76 	lcall  $0x76ff,$0xffffeb5e
 8049600:	ba 1b ce 3f 72       	mov    $0x723fce1b,%edx
 8049605:	ba 77 44 5f 5f       	mov    $0x5f5f4477,%edx
 804960a:	fb                   	sti    
 804960b:	f7 45 e9 ff ff ff 76 	testl  $0x76ffffff,-0x17(%ebp)
 8049612:	38 76 21             	cmp    %dh,0x21(%esi)
 8049615:	76 2e                	jbe    8049645 <powl@plt+0x585>
 8049617:	0c 5a                	or     $0x5a,%al
 8049619:	38 ba 7b ff ff ff    	cmp    %bh,-0x85(%edx)
 804961f:	ff 14 9a             	call   *(%edx,%ebx,4)
 8049622:	74 ba                	je     80495de <powl@plt+0x51e>
 8049624:	7b 74                	jnp    804969a <powl@plt+0x5da>
 8049626:	ab                   	stos   %eax,%es:(%edi)
 8049627:	3a 73 74             	cmp    0x74(%ebx),%dh
 804962a:	bb 3a 77 74 b2       	mov    $0xb274773a,%ebx
 804962f:	7b 7c                	jnp    80496ad <powl@plt+0x5ed>
 8049631:	3e f4                	ds hlt 
 8049633:	76 34                	jbe    8049669 <powl@plt+0x5a9>
 8049635:	74 72                	je     80496a9 <powl@plt+0x5e9>
 8049637:	8b 00                	mov    (%eax),%eax
 8049639:	00 00                	add    %al,(%eax)
 804963b:	fe                   	(bad)  
 804963c:	26 f0 49             	es lock dec %ecx
 804963f:	f6 f0                	div    %al
 8049641:	41                   	inc    %ecx
 8049642:	36 7c 13             	ss jl  8049658 <powl@plt+0x598>
 8049645:	f3 ad                	rep lods %ds:(%esi),%eax
 8049647:	af                   	scas   %es:(%edi),%eax
 8049648:	ae                   	scas   %es:(%edi),%al
 8049649:	97                   	xchg   %eax,%edi
 804964a:	cf                   	iret   
 804964b:	ff                   	(bad)  
 804964c:	ff                   	(bad)  
 804964d:	ff 97 a1 6b fb f7    	call   *-0x804945f(%edi)
 8049653:	17                   	pop    %ss
 8049654:	2c 04                	sub    $0x4,%al
 8049656:	00 00                	add    %al,(%eax)
 8049658:	7c 3b                	jl     8049695 <powl@plt+0x5d5>
 804965a:	df 7a 3f             	fistpll 0x3f(%edx)
 804965d:	8a f8                	mov    %al,%bh
 804965f:	47                   	inc    %edi
 8049660:	ff                   	(bad)  
 8049661:	ff                   	(bad)  
 8049662:	ff                   	(bad)  
 8049663:	ff 14 d3             	call   *(%ebx,%edx,8)
 8049666:	74 7a                	je     80496e2 <powl@plt+0x622>
 8049668:	8b 00                	mov    (%eax),%eax
 804966a:	00 00                	add    %al,(%eax)
 804966c:	7c 3f                	jl     80496ad <powl@plt+0x5ed>
 804966e:	ee                   	out    %al,(%dx)
 804966f:	f0 49                	lock dec %ecx
 8049671:	ff f0                	push   %eax
 8049673:	41                   	inc    %ecx
 8049674:	3f                   	aas    
 8049675:	7c 1f                	jl     8049696 <powl@plt+0x5d6>
 8049677:	fe                   	(bad)  
 8049678:	7a 3f                	jp     80496b9 <powl@plt+0x5f9>
 804967a:	8a f8                	mov    %al,%bh
 804967c:	47                   	inc    %edi
 804967d:	ff                   	(bad)  
 804967e:	ff                   	(bad)  
 804967f:	ff                   	(bad)  
 8049680:	ff 14 f0             	call   *(%eax,%esi,8)
 8049683:	7c ba                	jl     804963f <powl@plt+0x57f>
 8049685:	7b fe                	jnp    8049685 <powl@plt+0x5c5>
 8049687:	7c 82                	jl     804960b <powl@plt+0x54b>
 8049689:	7b f5                	jnp    8049680 <powl@plt+0x5c0>
 804968b:	81 6a 47 fe ff ff ff 	subl   $0xfffffffe,0x47(%edx)
 8049692:	74 aa                	je     804963e <powl@plt+0x57e>
 8049694:	1b 9a cc ea eb ff    	sbb    -0x141534(%edx),%ebx
 804969a:	ff                   	(bad)  
 804969b:	ff 8b fa 17 32 06    	decl   0x63217fa(%ebx)
 80496a1:	00 00                	add    %al,(%eax)
 80496a3:	72 9a                	jb     804963f <powl@plt+0x57f>
 80496a5:	0b a4 a1 5f 5d c3 11 	or     0x11c35d5f(%ecx,%eiz,4),%esp
 80496ac:	cc                   	int3   
 80496ad:	a4                   	movsb  %ds:(%esi),%es:(%edi)
 80496ae:	17                   	pop    %ss
 80496af:	c7                   	(bad)  
 80496b0:	a9 55 83 01 b1       	test   $0xb1018355,%eax
 80496b5:	47                   	inc    %edi
 80496b6:	44                   	inc    %esp
 80496b7:	44                   	inc    %esp
 80496b8:	45                   	inc    %ebp
 80496b9:	86 01                	xchg   %al,(%ecx)
 80496bb:	b4 44                	mov    $0x44,%ah
 80496bd:	41                   	inc    %ecx
 80496be:	44                   	inc    %esp
 80496bf:	44                   	inc    %esp
 80496c0:	ae                   	scas   %es:(%edi),%al
 80496c1:	7b cf                	jnp    8049692 <powl@plt+0x5d2>
 80496c3:	01 b5 c2 84 40 cc    	add    %esi,-0x33bf7b3e(%ebp)
 80496c9:	83 cf 01             	or     $0x1,%edi
 80496cc:	5d                   	pop    %ebp
 80496cd:	40                   	inc    %eax
 80496ce:	94                   	xchg   %eax,%esp
 80496cf:	4b                   	dec    %ebx
 80496d0:	f3 41                	repz inc %ecx
 80496d2:	4b                   	dec    %ebx
 80496d3:	fa                   	cli    
 80496d4:	9d                   	popf   
 80496d5:	c2 a8 40             	ret    $0x40a8
 80496d8:	ba 34 b4 2c 73       	mov    $0x732cb434,%edx
 80496dd:	41                   	inc    %ecx
 80496de:	44                   	inc    %esp
 80496df:	44                   	inc    %esp
 80496e0:	2d c4 d7 40 4d       	sub    $0x4d40d7c4,%eax
 80496e5:	a9 05 bf ba be       	test   $0xbebabf05,%eax
 80496ea:	c7 80 55 78 87 30 42 	movl   $0x4444f942,0x30877855(%eax)
 80496f1:	f9 44 44 
 80496f4:	45                   	inc    %ebp
 80496f5:	41                   	inc    %ecx
 80496f6:	af                   	scas   %es:(%edi),%eax
 80496f7:	55                   	push   %ebp
 80496f8:	c6 04 b4 45          	movb   $0x45,(%esp,%esi,4)
 80496fc:	ce                   	into   
 80496fd:	04 b4                	add    $0xb4,%al
 80496ff:	7f 00                	jg     8049701 <powl@plt+0x641>
 8049701:	b5 3a                	mov    $0x3a,%ch
 8049703:	fa                   	cli    
 8049704:	fd                   	std    
 8049705:	40                   	inc    %eax
 8049706:	44                   	inc    %esp
 8049707:	44                   	inc    %esp
 8049708:	45                   	inc    %ebp
 8049709:	ca 19 fc             	lret   $0xfc19
 804970c:	c9                   	leave  
 804970d:	c3                   	ret    
 804970e:	17                   	pop    %ss
 804970f:	b9 d5 c1 ae 28       	mov    $0x28aec1d5,%ecx
 8049714:	b3 3f                	mov    $0x3f,%bl
 8049716:	5a                   	pop    %edx
 8049717:	31 4f 62             	xor    %ecx,0x62(%edi)
 804971a:	c9                   	leave  
 804971b:	75 2c                	jne    8049749 <powl@plt+0x689>
 804971d:	c9                   	leave  
 804971e:	42                   	inc    %edx
 804971f:	b3 dc                	mov    $0xdc,%bl
 8049721:	4a                   	dec    %edx
 8049722:	12 58 c8             	adc    -0x38(%eax),%bl
 8049725:	e2 46                	loop   804976d <powl@plt+0x6ad>
 8049727:	38 d8                	cmp    %bl,%al
 8049729:	61                   	popa   
 804972a:	bb cf cf c1 86       	mov    $0x86c1cfcf,%ebx
 804972f:	20 b3 ae 4e 5a 30    	and    %dh,0x305a4eae(%ebx)
 8049735:	aa                   	stos   %al,%es:(%edi)
 8049736:	04 c9                	add    $0xc9,%al
 8049738:	cf                   	iret   
 8049739:	bd 85 75 c4 42       	mov    $0x42c47585,%ebp
 804973e:	42                   	inc    %edx
 804973f:	30 30                	xor    %dh,(%eax)
 8049741:	c9                   	leave  
 8049742:	07                   	pop    %es
 8049743:	2c b3                	sub    $0xb3,%al
 8049745:	82 46 bb 30          	addb   $0x30,-0x45(%esi)
 8049749:	c1 ae 34 60 2a 53 30 	shrl   $0x30,0x532a6034(%esi)
 8049750:	30 42 2a             	xor    %al,0x2a(%edx)
 8049753:	90                   	nop
 8049754:	a2 46 4a d8 ff       	mov    %al,0xffd84a46
 8049759:	b8 bd cf b3 86       	mov    $0x86b3cfbd,%eax
 804975e:	52                   	push   %edx
 804975f:	31 75 b6             	xor    %esi,-0x4a(%ebp)
 8049762:	c9                   	leave  
 8049763:	75 2c                	jne    8049791 <powl@plt+0x6d1>
 8049765:	c1 82 34 bb 42 c1 dc 	roll   $0xdc,-0x3ebd44cc(%edx)
 804976c:	34 12                	xor    $0x12,%al
 804976e:	2a 21                	sub    (%ecx),%ah
 8049770:	30 42 42             	xor    %al,0x42(%edx)
 8049773:	58                   	pop    %eax
 8049774:	d5 d0                	aad    $0xd0
 8049776:	46                   	inc    %esi
 8049777:	38 d8                	cmp    %bl,%al
 8049779:	ec                   	in     (%dx),%al
 804977a:	b8 cf cf c1 86       	mov    $0x86c1cfcf,%eax
 804977f:	20 31                	and    %dh,(%ecx)
 8049781:	07                   	pop    %es
 8049782:	b6 bb                	mov    $0xbb,%dh
 8049784:	75 5e                	jne    80497e4 <powl@plt+0x724>
 8049786:	c1 f0 34             	shl    $0x34,%eax
 8049789:	c9                   	leave  
 804978a:	42                   	inc    %edx
 804978b:	b3 dc                	mov    $0xdc,%bl
 804978d:	46                   	inc    %esi
 804978e:	12 58 27             	adc    0x27(%eax),%bl
 8049791:	42                   	inc    %edx
 8049792:	42                   	inc    %edx
 8049793:	30 58 6b             	xor    %bl,0x6b(%eax)
 8049796:	d1 34 38             	shll   (%eax,%edi,1)
 8049799:	aa                   	stos   %al,%es:(%edi)
 804979a:	cf                   	iret   
 804979b:	ca cf bd             	lret   $0xbdcf
 804979e:	c1 f4 20             	shl    $0x20,%esp
 80497a1:	43                   	inc    %ebx
 80497a2:	07                   	pop    %es
 80497a3:	c4 bb 07 5e b3 f0    	les    -0xf4ca1f9(%ebx),%edi
 80497a9:	46                   	inc    %esi
 80497aa:	c9                   	leave  
 80497ab:	30 b3 ae 46 60 58    	xor    %dh,0x586046ae(%ebx)
 80497b1:	5a                   	pop    %edx
 80497b2:	42                   	inc    %edx
 80497b3:	30 30                	xor    %dh,(%eax)
 80497b5:	2a e9                	sub    %cl,%ch
 80497b7:	a6                   	cmpsb  %es:(%edi),%ds:(%esi)
 80497b8:	34 4a                	xor    $0x4a,%al
 80497ba:	aa                   	stos   %al,%es:(%edi)
 80497bb:	5c                   	pop    %esp
 80497bc:	ca bd bd             	lret   $0xbdbd
 80497bf:	b3 f4                	mov    $0xf4,%bl
 80497c1:	52                   	push   %edx
 80497c2:	43                   	inc    %ebx
 80497c3:	75 c4                	jne    8049789 <powl@plt+0x6c9>
 80497c5:	c9                   	leave  
 80497c6:	07                   	pop    %es
 80497c7:	2c b3                	sub    $0xb3,%al
 80497c9:	82 46 bb 30          	addb   $0x30,-0x45(%esi)
 80497cd:	c1 ae 34 60 2a 73 30 	shrl   $0x30,0x732a6034(%esi)
 80497d4:	30 42 2a             	xor    %al,0x2a(%edx)
 80497d7:	d4 a5                	aam    $0xa5
 80497d9:	46                   	inc    %esi
 80497da:	4a                   	dec    %edx
 80497db:	d8 7b b8             	fdivrs -0x48(%ebx)
 80497de:	bd cf b3 86 52       	mov    $0x5286b3cf,%ebp
 80497e3:	31 75 b6             	xor    %esi,-0x4a(%ebp)
 80497e6:	c9                   	leave  
 80497e7:	75 2c                	jne    8049815 <powl@plt+0x755>
 80497e9:	c1 82 34 bb 42 28 30 	roll   $0x30,0x2842bb34(%edx)
 80497f0:	60                   	pusha  
 80497f1:	2a 65 30             	sub    0x30(%ebp),%ah
 80497f4:	30 42 2a             	xor    %al,0x2a(%edx)
 80497f7:	76 a5                	jbe    804979e <powl@plt+0x6de>
 80497f9:	46                   	inc    %esi
 80497fa:	4a                   	dec    %edx
 80497fb:	d8 1b                	fcomps (%ebx)
 80497fd:	b8 bd cf b3 86       	mov    $0x86b3cfbd,%eax
 8049802:	52                   	push   %edx
 8049803:	31 75 b6             	xor    %esi,-0x4a(%ebp)
 8049806:	c9                   	leave  
 8049807:	75 2c                	jne    8049835 <powl@plt+0x775>
 8049809:	c1 82 34 bb 42 c1 dc 	roll   $0xdc,-0x3ebd44cc(%edx)
 8049810:	34 12                	xor    $0x12,%al
 8049812:	2a 39                	sub    (%ecx),%bh
 8049814:	30 42 42             	xor    %al,0x42(%edx)
 8049817:	58                   	pop    %eax
 8049818:	2f                   	das    
 8049819:	d7                   	xlat   %ds:(%ebx)
 804981a:	46                   	inc    %esi
 804981b:	38 d8                	cmp    %bl,%al
 804981d:	48                   	dec    %eax
 804981e:	b8 cf cf c1 86       	mov    $0x86c1cfcf,%eax
 8049823:	20 31                	and    %dh,(%ecx)
 8049825:	07                   	pop    %es
 8049826:	b6 b3                	mov    $0xb3,%dh
 8049828:	4d                   	dec    %ebp
 8049829:	b6 45                	mov    $0x45,%dh
 804982b:	45                   	inc    %ebp
 804982c:	2b c9                	sub    %ecx,%ecx
 804982e:	07                   	pop    %es
 804982f:	2c b3                	sub    $0xb3,%al
 8049831:	82 46 bb 30          	addb   $0x30,-0x45(%esi)
 8049835:	c1 ae 38 60 2a 52 91 	shrl   $0x91,0x522a6038(%esi)
 804983c:	34 4a                	xor    $0x4a,%al
 804983e:	aa                   	stos   %al,%es:(%edi)
 804983f:	3d c8 bd bd b3       	cmp    $0xb3bdbdc8,%eax
 8049844:	f4                   	hlt    
 8049845:	52                   	push   %edx
 8049846:	a9 20 b3 ae 4e       	test   $0x4eaeb320,%eax
 804984b:	58                   	pop    %eax
 804984c:	08 e3                	or     %ah,%bl
 804984e:	46                   	inc    %esi
 804984f:	38 d8                	cmp    %bl,%al
 8049851:	b9 b5 cf cf c1       	mov    $0xc1cfcfb5,%ecx
 8049856:	86 20                	xchg   %ah,(%eax)
 8049858:	a0 8b c3 8d 4c       	mov    0x4c8dc38b,%al
 804985d:	24 04                	and    $0x4,%al
 804985f:	83 e4 f0             	and    $0xfffffff0,%esp
 8049862:	ff 71 fc             	pushl  -0x4(%ecx)
 8049865:	55                   	push   %ebp
 8049866:	89 e5                	mov    %esp,%ebp
 8049868:	51                   	push   %ecx
 8049869:	83 ec 04             	sub    $0x4,%esp
 804986c:	89 c8                	mov    %ecx,%eax
 804986e:	ff 70 04             	pushl  0x4(%eax)
 8049871:	ff 30                	pushl  (%eax)
 8049873:	68 53 00 00 00       	push   $0x53
 8049878:	68 0e 97 04 08       	push   $0x804970e
 804987d:	e8 a9 f9 ff ff       	call   804922b <powl@plt+0x16b>
 8049882:	83 c4 10             	add    $0x10,%esp
 8049885:	b8 00 00 00 00       	mov    $0x0,%eax
 804988a:	8b 4d fc             	mov    -0x4(%ebp),%ecx
 804988d:	c9                   	leave  
 804988e:	8d 61 fc             	lea    -0x4(%ecx),%esp
 8049891:	c3                   	ret    
 8049892:	66 90                	xchg   %ax,%ax
 8049894:	66 90                	xchg   %ax,%ax
 8049896:	66 90                	xchg   %ax,%ax
 8049898:	66 90                	xchg   %ax,%ax
 804989a:	66 90                	xchg   %ax,%ax
 804989c:	66 90                	xchg   %ax,%ax
 804989e:	66 90                	xchg   %ax,%ax
 80498a0:	55                   	push   %ebp
 80498a1:	57                   	push   %edi
 80498a2:	56                   	push   %esi
 80498a3:	53                   	push   %ebx
 80498a4:	e8 77 f8 ff ff       	call   8049120 <powl@plt+0x60>
 80498a9:	81 c3 57 27 00 00    	add    $0x2757,%ebx
 80498af:	83 ec 0c             	sub    $0xc,%esp
 80498b2:	8b 6c 24 28          	mov    0x28(%esp),%ebp
 80498b6:	e8 45 f7 ff ff       	call   8049000 <strstr@plt-0x30>
 80498bb:	8d b3 00 ff ff ff    	lea    -0x100(%ebx),%esi
 80498c1:	8d 83 fc fe ff ff    	lea    -0x104(%ebx),%eax
 80498c7:	29 c6                	sub    %eax,%esi
 80498c9:	c1 fe 02             	sar    $0x2,%esi
 80498cc:	74 1f                	je     80498ed <powl@plt+0x82d>
 80498ce:	31 ff                	xor    %edi,%edi
 80498d0:	83 ec 04             	sub    $0x4,%esp
 80498d3:	55                   	push   %ebp
 80498d4:	ff 74 24 2c          	pushl  0x2c(%esp)
 80498d8:	ff 74 24 2c          	pushl  0x2c(%esp)
 80498dc:	ff 94 bb fc fe ff ff 	call   *-0x104(%ebx,%edi,4)
 80498e3:	83 c7 01             	add    $0x1,%edi
 80498e6:	83 c4 10             	add    $0x10,%esp
 80498e9:	39 fe                	cmp    %edi,%esi
 80498eb:	75 e3                	jne    80498d0 <powl@plt+0x810>
 80498ed:	83 c4 0c             	add    $0xc,%esp
 80498f0:	5b                   	pop    %ebx
 80498f1:	5e                   	pop    %esi
 80498f2:	5f                   	pop    %edi
 80498f3:	5d                   	pop    %ebp
 80498f4:	c3                   	ret    
 80498f5:	8d b4 26 00 00 00 00 	lea    0x0(%esi,%eiz,1),%esi
 80498fc:	8d 74 26 00          	lea    0x0(%esi,%eiz,1),%esi
 8049900:	c3                   	ret    
