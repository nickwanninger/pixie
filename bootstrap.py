mid0 = (u"""(defprotocol ISeq""", "<unknown>", 4)
mid1 = (u"""(defprotocol ISeqable""", "<unknown>", 8)
mid2 = (u"""(defprotocol ICounted""", "<unknown>", 11)
mid3 = (u"""(defprotocol IIndexed""", "<unknown>", 14)
mid4 = (u"""(defprotocol IPersistentCollection""", "<unknown>", 19)
mid5 = (u"""(defprotocol IEmpty""", "<unknown>", 23)
mid6 = (u"""(defprotocol IObject""", "<unknown>", 26)
mid7 = (u"""(defprotocol IReduce""", "<unknown>", 32)
mid8 = (u"""(defprotocol IDeref""", "<unknown>", 35)
mid9 = (u"""(defprotocol IReset""", "<unknown>", 38)
mid10 = (u"""(defprotocol INamed""", "<unknown>", 41)
mid11 = (u"""(defprotocol IAssociative""", "<unknown>", 45)
mid12 = (u"""(defprotocol ILookup""", "<unknown>", 50)
mid13 = (u"""(defprotocol IMapEntry""", "<unknown>", 53)
mid14 = (u"""(defprotocol IStack""", "<unknown>", 57)
mid15 = (u"""(defprotocol IPop""", "<unknown>", 60)
mid16 = (u"""(defprotocol IFn""", "<unknown>", 63)
mid17 = (u"""(defprotocol IDoc""", "<unknown>", 66)
mid18 = (u"""(defprotocol IMeta""", "<unknown>", 73)
mid19 = (u"""(defprotocol ITransientCollection""", "<unknown>", 77)
mid20 = (u"""(defprotocol IToTransient""", "<unknown>", 80)
mid21 = (u"""(defprotocol ITransientStack""", "<unknown>", 83)
mid22 = (u"""(defprotocol IDisposable""", "<unknown>", 87)
mid23 = (u"""(defprotocol IMessageObject""", "<unknown>", 90)
mid24 = (u"""(extend -get-field Object -internal-get-field)""", "<unknown>", 96)
mid25 = (u"""(extend -str Object (fn [x sb]""", "<unknown>", 97)
mid26 = (u"""                      (sb (-internal-to-str x))))""", "<unknown>", 98)
mid27 = (u"""(extend -repr Object (fn [x sb]""", "<unknown>", 99)
mid28 = (u"""                       (sb (-internal-to-repr x))))""", "<unknown>", 100)
mid29 = (u"""  (-str [this sb]""", "<unknown>", 105)
mid30 = (u"""(extend-type String""", "<unknown>", 103)
mid31 = (u"""    (sb this)))""", "<unknown>", 106)
mid32 = (u"""(extend -eq Number -num-eq)""", "<unknown>", 110)
mid33 = (u"""  ([x] x)""", "<unknown>", 117)
mid34 = (u"""  ([x y] (-add x y))""", "<unknown>", 118)
mid35 = (u"""   (-apply + (+ x y) more)))""", "<unknown>", 120)
mid36 = (u"""  ([x] x)""", "<unknown>", 124)
mid37 = (u"""  ([x y] (-sub x y))""", "<unknown>", 125)
mid38 = (u"""   (-apply - (- x y) more))) """, "<unknown>", 127)
mid39 = (u"""  ([x] (+ x 1)))""", "<unknown>", 130)
mid40 = (u"""  ([x] (- x 1)))""", "<unknown>", 133)
mid41 = (u"""  ([x y] (-lt x y))""", "<unknown>", 136)
mid42 = (u"""   (-apply < (< x y) more)))""", "<unknown>", 138)
mid43 = (u"""  ([x y] (-gt x y))""", "<unknown>", 141)
mid44 = (u"""   (-apply > (> x y) more)))""", "<unknown>", 143)
mid45 = (u"""  ([x y] (if (identical? x y)""", "<unknown>", 151)
mid46 = (u"""           (-eq x y)))""", "<unknown>", 153)
mid47 = (u"""  ([x y & rest] (if (eq x y)""", "<unknown>", 154)
mid48 = (u"""                  (apply = y rest)""", "<unknown>", 155)
mid49 = (u"""  ([coll] coll)""", "<unknown>", 160)
mid50 = (u"""  ([coll itm] (-conj coll itm))""", "<unknown>", 161)
mid51 = (u"""   (-apply conj (conj x y) more)))""", "<unknown>", 163)
mid52 = (u"""  ([coll] (-count coll)))""", "<unknown>", 167)
mid53 = (u"""(deftype Cons [first next meta]""", "<unknown>", 170)
mid54 = (u"""  (-first [this] first)""", "<unknown>", 172)
mid55 = (u"""  (-next [this] next)""", "<unknown>", 173)
mid56 = (u"""  (-seq [this] this)""", "<unknown>", 175)
mid57 = (u"""  (-meta [this] meta)""", "<unknown>", 177)
mid58 = (u"""  (-with-meta [this new-meta]""", "<unknown>", 178)
mid59 = (u"""    (->Cons first next new-meta)))""", "<unknown>", 179)
mid60 = (u"""  (->Cons head (seq tail) nil))""", "<unknown>", 182)
mid61 = (u"""  ([] (-string-builder))""", "<unknown>", 187)
mid62 = (u"""  ([sb] (-str sb))""", "<unknown>", 188)
mid63 = (u"""   (if (instance? String x)""", "<unknown>", 190)
mid64 = (u"""     (-add-to-string-builder x)""", "<unknown>", 191)
mid65 = (u"""     (-add-to-string-bulder (-str x)))))""", "<unknown>", 192)
mid66 = (u"""  (transduce""", "<unknown>", 195)
mid67 = (u"""   (map str)""", "<unknown>", 196)
mid68 = (u"""   string-builder""", "<unknown>", 197)
mid69 = (u"""   args))""", "<unknown>", 198)
mid70 = (u"""  (let [sb (-string-builder)""", "<unknown>", 201)
mid71 = (u"""                 (-add-to-string-builder sb x))]""", "<unknown>", 203)
mid72 = (u"""           sb sb]""", "<unknown>", 205)
mid73 = (u"""    (loop [idx 0""", "<unknown>", 204)
mid74 = (u"""      (if (< idx (count args))""", "<unknown>", 206)
mid75 = (u"""        (recur (inc idx)""", "<unknown>", 207)
mid76 = (u"""               (do (-str (aget args idx) add-fn)""", "<unknown>", 208)
mid77 = (u"""                   (add-fn " ")""", "<unknown>", 209)
mid78 = (u"""                 sb))""", "<unknown>", 210)
mid79 = (u"""        (-blocking-println (-finish-string-builder sb))))""", "<unknown>", 211)
mid80 = (u"""  (if (-satisfies? ISeqable t)""", "<unknown>", 225)
mid81 = (u"""    (let [ts (seq t)]""", "<unknown>", 226)
mid82 = (u"""      (if (not ts) false""", "<unknown>", 227)
mid83 = (u"""          (if (-instance? (first ts) x)""", "<unknown>", 228)
mid84 = (u"""            (instance? (rest ts) x))))""", "<unknown>", 230)
mid85 = (u"""    (-instance? t x)))""", "<unknown>", 231)
mid86 = (u"""(deftype Reduced [x]""", "<unknown>", 237)
mid87 = (u"""  (-deref [this] x))""", "<unknown>", 239)
mid88 = (u"""  (->Reduced x))""", "<unknown>", 242)
mid89 = (u"""  (instance? Reduced x))""", "<unknown>", 245)
mid90 = (u"""  (if (-satisfies? ISeqable p)""", "<unknown>", 258)
mid91 = (u"""    (let [ps (seq p)]""", "<unknown>", 259)
mid92 = (u"""      (if (not ps) true""", "<unknown>", 260)
mid93 = (u"""          (if (not (-satisfies? (first ps) x))""", "<unknown>", 261)
mid94 = (u"""            (satisfies? (rest ps) x))))""", "<unknown>", 263)
mid95 = (u"""    (-satisfies? p x)))""", "<unknown>", 264)
mid96 = (u"""   (let [f (xform rf)""", "<unknown>", 275)
mid97 = (u"""         result (-reduce coll f (f))]""", "<unknown>", 276)
mid98 = (u"""     (f result)))""", "<unknown>", 277)
mid99 = (u"""   (let [result (-reduce coll f (f))]""", "<unknown>", 272)
mid100 = (u"""     (f result)))""", "<unknown>", 273)
mid101 = (u"""   (let [f (xform rf)""", "<unknown>", 279)
mid102 = (u"""         result (-reduce coll f init)]""", "<unknown>", 280)
mid103 = (u"""     (f result))))""", "<unknown>", 281)
mid104 = (u"""   (-reduce col rf init)))""", "<unknown>", 287)
mid105 = (u"""   (reduce rf (rf) col))""", "<unknown>", 285)
mid106 = (u"""   (if (satisfies? IToTransient to)""", "<unknown>", 298)
mid107 = (u"""     (transduce xform conj! (transient to) from)""", "<unknown>", 299)
mid108 = (u"""     (transduce xform conj to from))))""", "<unknown>", 300)
mid109 = (u"""   (if (satisfies? IToTransient to)""", "<unknown>", 294)
mid110 = (u"""     (persistent! (reduce conj! (transient to) from))""", "<unknown>", 295)
mid111 = (u"""     (reduce conj to from)))""", "<unknown>", 296)
mid112 = (u"""       ([] (xf))""", "<unknown>", 309)
mid113 = (u"""       ([result] (xf result))""", "<unknown>", 310)
mid114 = (u"""       ([result item] (xf result (f item))))))""", "<unknown>", 311)
mid115 = (u"""   (lazy-seq*""", "<unknown>", 313)
mid116 = (u"""      (let [s (seq coll)]""", "<unknown>", 315)
mid117 = (u"""        (if s""", "<unknown>", 316)
mid118 = (u"""          (cons (f (first s))""", "<unknown>", 317)
mid119 = (u"""                (map f (rest s)))""", "<unknown>", 318)
mid120 = (u"""                (lazy-seq*""", "<unknown>", 322)
mid121 = (u"""                   (let [ss (map seq cs)]""", "<unknown>", 324)
mid122 = (u"""                     (if (every? identity ss)""", "<unknown>", 325)
mid123 = (u"""                       (cons (map first ss) (step (map rest ss)))""", "<unknown>", 326)
mid124 = (u"""     (map (fn [args] (apply f args)) (step colls)))))""", "<unknown>", 328)
mid125 = (u"""   (let [step (fn step [cs]""", "<unknown>", 321)
mid126 = (u"""(deftype Range [start stop step]""", "<unknown>", 334)
mid127 = (u"""  (-reduce [self f init]""", "<unknown>", 336)
mid128 = (u"""           acc init]""", "<unknown>", 338)
mid129 = (u"""    (loop [i start""", "<unknown>", 337)
mid130 = (u"""      (println i)""", "<unknown>", 339)
mid131 = (u"""      (if (or (and (> step 0) (< i stop))""", "<unknown>", 340)
mid132 = (u"""              (and (< step 0) (> i stop))""", "<unknown>", 341)
mid133 = (u"""              (and (= step 0)))""", "<unknown>", 342)
mid134 = (u"""        (let [acc (f acc i)]""", "<unknown>", 343)
mid135 = (u"""          (if (reduced? acc)""", "<unknown>", 344)
mid136 = (u"""            @acc""", "<unknown>", 345)
mid137 = (u"""            (recur (+ i step) acc)))""", "<unknown>", 346)
mid138 = (u"""        acc)))""", "<unknown>", 347)
mid139 = (u"""  (-count [self]""", "<unknown>", 349)
mid140 = (u"""    (if (or (and (< start stop) (< step 0))""", "<unknown>", 350)
mid141 = (u"""            (and (> start stop) (> step 0))""", "<unknown>", 351)
mid142 = (u"""            (= step 0))""", "<unknown>", 352)
mid143 = (u"""      (abs (quot (- start stop) step))))""", "<unknown>", 354)
mid144 = (u"""  (-nth [self idx]""", "<unknown>", 356)
mid145 = (u"""    (when (or (= start stop 0) (neg? idx))""", "<unknown>", 357)
mid146 = (u"""      (throw [:pixie.stdlib/OutOfRangeException "Index out of Range"]))""", "<unknown>", 358)
mid147 = (u"""  (-nth-not-found [self idx not-found]""", "<unknown>", 364)
mid148 = (u"""    (let [cmp (if (< start stop) < >)""", "<unknown>", 365)
mid149 = (u"""          val (+ start (* idx step))]""", "<unknown>", 366)
mid150 = (u"""      (if (cmp val stop)""", "<unknown>", 367)
mid151 = (u"""        val""", "<unknown>", 368)
mid152 = (u"""       not-found)))""", "<unknown>", 369)
mid153 = (u"""  (-seq [self]""", "<unknown>", 371)
mid154 = (u"""    (when (or (and (> step 0) (< start stop))""", "<unknown>", 372)
mid155 = (u"""              (and (< step 0) (> start stop)))""", "<unknown>", 373)
mid156 = (u"""      (cons start (lazy-seq* #(range (+ start step) stop step)))))""", "<unknown>", 374)
mid157 = (u"""  (-str [this sbf]""", "<unknown>", 376)
mid158 = (u"""    (-str (seq this) sbf))""", "<unknown>", 377)
mid159 = (u"""  (-repr [this sbf]""", "<unknown>", 378)
mid160 = (u"""    (-repr (seq this) sbf))""", "<unknown>", 379)
mid161 = (u"""  (-eq [this sb]))""", "<unknown>", 380)
mid162 = (u"""  ([] (->Range 0 MAX-NUMBER 1))""", "<unknown>", 392)
mid163 = (u"""  ([stop] (->Range 0 stop 1))""", "<unknown>", 393)
mid164 = (u"""  ([start stop step] (->Range start stop step)))""", "<unknown>", 395)
mid165 = (u"""  ([start stop] (->Range start stop 1))""", "<unknown>", 394)
mid166 = (u"""(deftype Node [edit array]""", "<unknown>", 401)
mid167 = (u"""  (-get-field [this name]""", "<unknown>", 403)
mid168 = (u"""    (get-field this name)))""", "<unknown>", 404)
mid169 = (u"""   (new-node edit (array 32)))""", "<unknown>", 408)
mid170 = (u"""   (->Node edit array)))""", "<unknown>", 410)
mid171 = (u"""(def EMPTY-NODE (new-node nil))""", "<unknown>", 412)
mid172 = (u"""  (let [cnt (.-cnt this)]""", "<unknown>", 417)
mid173 = (u"""    (if (< cnt 32)""", "<unknown>", 418)
mid174 = (u"""      (bit-shift-left (bit-shift-right (dec cnt) 5) 5))))""", "<unknown>", 420)
mid175 = (u"""      (if (and (<= 0 i) (< i cnt))""", "<unknown>", 423)
mid176 = (u"""        (if (>= i (tailoff this))""", "<unknown>", 424)
mid177 = (u"""          tail""", "<unknown>", 425)
mid178 = (u"""                      (if (> level 0)""", "<unknown>", 427)
mid179 = (u"""                        (look-deeper (aget (:array node)""", "<unknown>", 428)
mid180 = (u"""                                           (bit-and (bit-shift-right i level) 0x01f))""", "<unknown>", 429)
mid181 = (u"""                                     (- level 5))""", "<unknown>", 430)
mid182 = (u"""                        (:array node)))""", "<unknown>", 431)
mid183 = (u"""                    root""", "<unknown>", 432)
mid184 = (u"""                    shift)))))""", "<unknown>", 433)
mid185 = (u"""          (.-array ((fn look-deeper [node level]""", "<unknown>", 426)
mid186 = (u"""(deftype PersistentVector [cnt shift root tail meta]""", "<unknown>", 435)
mid187 = (u"""  (-get-field [this name]""", "<unknown>", 437)
mid188 = (u"""    (get-field this name))""", "<unknown>", 438)
mid189 = (u"""  (-conj [this val]""", "<unknown>", 441)
mid190 = (u"""    (assert (< cnt 0xFFFFFFFF) "Vector too large")""", "<unknown>", 442)
mid191 = (u"""  (-count [this] cnt))""", "<unknown>", 465)
mid192 = (u"""  (let [subidx (bit-and (bit-shift-right (dec (.-cnt this)) level) 0x01f)""", "<unknown>", 469)
mid193 = (u"""        ret-array (aclone (.-array parent))""", "<unknown>", 470)
mid194 = (u"""        node-to-insert (if (= level 5)""", "<unknown>", 471)
mid195 = (u"""                         tail-node""", "<unknown>", 472)
mid196 = (u"""                         (let [child (aget (.-array parent) subidx)]""", "<unknown>", 473)
mid197 = (u"""                           (if (= child nil)""", "<unknown>", 474)
mid198 = (u"""                             (new-path (.-edit (.-root this))""", "<unknown>", 475)
mid199 = (u"""                                       (- level 5)""", "<unknown>", 476)
mid200 = (u"""                                       tail-node)""", "<unknown>", 477)
mid201 = (u"""                             (push-tail this""", "<unknown>", 478)
mid202 = (u"""                                        (- level 5)""", "<unknown>", 479)
mid203 = (u"""                                        child""", "<unknown>", 480)
mid204 = (u"""                                        tail-node))))]""", "<unknown>", 481)
mid205 = (u"""    (aset ret-array subidx node-to-insert)""", "<unknown>", 482)
mid206 = (u"""    (->Node (.-edit parent) node-to-insert)))""", "<unknown>", 483)
mid207 = (u"""  (if (= level 0)""", "<unknown>", 486)
mid208 = (u"""    node""", "<unknown>", 487)
mid209 = (u"""    (->Node edit""", "<unknown>", 488)
mid210 = (u"""            (new-path edit (- level 5) node))))""", "<unknown>", 489)
mid211 = (u"""(def EMPTY (->PersistentVector 0 5 EMPTY-NODE (array 0) nil))""", "<unknown>", 492)
mid212 = (u"""  (if (< (count arr) 32)""", "<unknown>", 495)
mid213 = (u"""    (->PersistentVector (count arr) 5 EMPTY-NODE arr nil)""", "<unknown>", 496)
mid214 = (u"""    (into [] arr)))""", "<unknown>", 497)
mid215 = (u"""  (-reduce [this f init]""", "<unknown>", 510)
mid216 = (u"""(extend-type Array""", "<unknown>", 501)
mid217 = (u"""           acc init]""", "<unknown>", 512)
mid218 = (u"""    (loop [idx 0""", "<unknown>", 511)
mid219 = (u"""      (if (reduced? acc)""", "<unknown>", 513)
mid220 = (u"""        @acc""", "<unknown>", 514)
mid221 = (u"""        (if (< idx (count this))""", "<unknown>", 515)
mid222 = (u"""          (recur (inc idx)""", "<unknown>", 516)
mid223 = (u"""                 (f acc (aget this idx)))""", "<unknown>", 517)
mid224 = (u"""          acc)))))""", "<unknown>", 518)
mid225 = (u"""  (-count ([arr]""", "<unknown>", 506)
mid226 = (u"""           (.-count arr)))""", "<unknown>", 507)
mid227 = (u"""  (-conj ([arr itm]""", "<unknown>", 503)
mid228 = (u"""          (conj (vector-from-array arr) itm)))""", "<unknown>", 504)
mid229 = (u"""(println 42)""", "<unknown>", 523)
mid230 = (u"""(into [] (range 1000))""", "<unknown>", 525)
mid231 = (u"""(do ;; This file is used to build what we need to even start running stdlib.pxi""", "<unknown>", 1)

 
code_ast=i.Do(
  args=[
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/ISeq)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"ISeq")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"ISeq")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-first)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-first")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-first")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"ISeq"), meta=i.Meta(mid0, 14)),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-next)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-next")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-next")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"ISeq"), meta=i.Meta(mid0, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid0, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/ISeqable)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"ISeqable")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"ISeqable")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-seq)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-seq")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-seq")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"ISeqable"), meta=i.Meta(mid1, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid1, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/ICounted)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"ICounted")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"ICounted")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-count)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-count")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-count")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"ICounted"), meta=i.Meta(mid2, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid2, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/IIndexed)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"IIndexed")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"IIndexed")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-nth)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-nth")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-nth")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IIndexed"), meta=i.Meta(mid3, 14)),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-nth-not-found)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-nth-not-found")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-nth-not-found")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IIndexed"), meta=i.Meta(mid3, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid3, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/IPersistentCollection)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"IPersistentCollection")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"IPersistentCollection")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-conj)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-conj")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-conj")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IPersistentCollection"), meta=i.Meta(mid4, 14)),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-disj)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-disj")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-disj")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IPersistentCollection"), meta=i.Meta(mid4, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid4, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/IEmpty)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"IEmpty")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"IEmpty")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-empty)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-empty")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-empty")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IEmpty"), meta=i.Meta(mid5, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid5, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/IObject)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"IObject")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"IObject")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-hash)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-hash")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-hash")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IObject"), meta=i.Meta(mid6, 14)),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-eq)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-eq")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-eq")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IObject"), meta=i.Meta(mid6, 14)),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-str)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-str")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-str")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IObject"), meta=i.Meta(mid6, 14)),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-repr)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-repr")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-repr")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IObject"), meta=i.Meta(mid6, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid6, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/IReduce)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"IReduce")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"IReduce")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-reduce)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-reduce")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-reduce")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IReduce"), meta=i.Meta(mid7, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid7, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/IDeref)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"IDeref")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"IDeref")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-deref)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-deref")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-deref")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IDeref"), meta=i.Meta(mid8, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid8, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/IReset)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"IReset")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"IReset")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-reset!)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-reset!")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-reset!")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IReset"), meta=i.Meta(mid9, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid9, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/INamed)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"INamed")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"INamed")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-namespace)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-namespace")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-namespace")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"INamed"), meta=i.Meta(mid10, 14)),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-name)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-name")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-name")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"INamed"), meta=i.Meta(mid10, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid10, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/IAssociative)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"IAssociative")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"IAssociative")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-assoc)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-assoc")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-assoc")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IAssociative"), meta=i.Meta(mid11, 14)),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-contains-key)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-contains-key")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-contains-key")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IAssociative"), meta=i.Meta(mid11, 14)),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-dissoc)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-dissoc")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-dissoc")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IAssociative"), meta=i.Meta(mid11, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid11, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/ILookup)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"ILookup")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"ILookup")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-get)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-get")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-get")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"ILookup"), meta=i.Meta(mid12, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid12, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/IMapEntry)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"IMapEntry")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"IMapEntry")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-key)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-key")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-key")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IMapEntry"), meta=i.Meta(mid13, 14)),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-val)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-val")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-val")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IMapEntry"), meta=i.Meta(mid13, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid13, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/IStack)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"IStack")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"IStack")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-push)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-push")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-push")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IStack"), meta=i.Meta(mid14, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid14, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/IPop)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"IPop")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"IPop")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-pop)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-pop")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-pop")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IPop"), meta=i.Meta(mid15, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid15, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/IFn)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"IFn")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"IFn")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-invoke)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-invoke")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-invoke")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IFn"), meta=i.Meta(mid16, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid16, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/IDoc)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"IDoc")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"IDoc")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-doc)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-doc")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-doc")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IDoc"), meta=i.Meta(mid17, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid17, 1)),
    i.Invoke(args=[
# (def pixie.stdlib/IVector)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"IVector")),
      i.Invoke(
        args=[
          i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
          i.Const(rt.wrap(u"IVector")),
        ],
        meta=nil)]),
    i.Invoke(args=[
# (def pixie.stdlib/ISequential)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"ISequential")),
      i.Invoke(
        args=[
          i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
          i.Const(rt.wrap(u"ISequential")),
        ],
        meta=nil)]),
    i.Invoke(args=[
# (def pixie.stdlib/IMap)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"IMap")),
      i.Invoke(
        args=[
          i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
          i.Const(rt.wrap(u"IMap")),
        ],
        meta=nil)]),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/IMeta)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"IMeta")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"IMeta")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-with-meta)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-with-meta")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-with-meta")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IMeta"), meta=i.Meta(mid18, 14)),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-meta)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-meta")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-meta")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IMeta"), meta=i.Meta(mid18, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid18, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/ITransientCollection)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"ITransientCollection")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"ITransientCollection")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-conj!)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-conj!")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-conj!")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"ITransientCollection"), meta=i.Meta(mid19, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid19, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/IToTransient)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"IToTransient")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"IToTransient")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-transient)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-transient")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-transient")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IToTransient"), meta=i.Meta(mid20, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid20, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/ITransientStack)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"ITransientStack")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"ITransientStack")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-push!)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-push!")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-push!")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"ITransientStack"), meta=i.Meta(mid21, 14)),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-pop!)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-pop!")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-pop!")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"ITransientStack"), meta=i.Meta(mid21, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid21, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/IDisposable)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"IDisposable")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"IDisposable")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-dispose!)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-dispose!")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-dispose!")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IDisposable"), meta=i.Meta(mid22, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid22, 1)),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/IMessageObject)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"IMessageObject")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"protocol"), meta=nil),
              i.Const(rt.wrap(u"IMessageObject")),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-get-field)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-get-field")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-get-field")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IMessageObject"), meta=i.Meta(mid23, 14)),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/-invoke-method)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"-invoke-method")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"polymorphic-fn"), meta=nil),
              i.Const(rt.wrap(u"-invoke-method")),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"IMessageObject"), meta=i.Meta(mid23, 14)),
            ],
            meta=nil)]),
      ],
    meta=i.Meta(mid23, 1)),
    i.Invoke(
      args=[
        i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=i.Meta(mid24, 2)),
        i.VDeref(code.intern_var(u"pixie.stdlib", u"-get-field"), meta=i.Meta(mid24, 9)),
        i.VDeref(code.intern_var(u"pixie.stdlib", u"Object"), meta=i.Meta(mid24, 20)),
        i.VDeref(code.intern_var(u"pixie.stdlib", u"-internal-get-field"), meta=i.Meta(mid24, 27)),
      ],
      meta=i.Meta(mid24, 1)),
    i.Invoke(
      args=[
        i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=i.Meta(mid25, 2)),
        i.VDeref(code.intern_var(u"pixie.stdlib", u"-str"), meta=i.Meta(mid25, 9)),
        i.VDeref(code.intern_var(u"pixie.stdlib", u"Object"), meta=i.Meta(mid25, 14)),
        i.Fn(args=[kw(u"x"),kw(u"sb")],name=kw(u"fn_348"),
          body=i.TailCall(
            args=[
              i.Lookup(kw(u"sb"), meta=i.Meta(mid26, 24)),
              i.Invoke(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"-internal-to-str"), meta=i.Meta(mid26, 28)),
                  i.Lookup(kw(u"x"), meta=i.Meta(mid26, 45)),
                ],
                meta=i.Meta(mid26, 27)),
            ],
            meta=i.Meta(mid26, 23)),
        ),
      ],
      meta=i.Meta(mid25, 1)),
    i.Invoke(
      args=[
        i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=i.Meta(mid27, 2)),
        i.VDeref(code.intern_var(u"pixie.stdlib", u"-repr"), meta=i.Meta(mid27, 9)),
        i.VDeref(code.intern_var(u"pixie.stdlib", u"Object"), meta=i.Meta(mid27, 15)),
        i.Fn(args=[kw(u"x"),kw(u"sb")],name=kw(u"fn_351"),
          body=i.TailCall(
            args=[
              i.Lookup(kw(u"sb"), meta=i.Meta(mid28, 25)),
              i.Invoke(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"-internal-to-repr"), meta=i.Meta(mid28, 29)),
                  i.Lookup(kw(u"x"), meta=i.Meta(mid28, 47)),
                ],
                meta=i.Meta(mid28, 28)),
            ],
            meta=i.Meta(mid28, 24)),
        ),
      ],
      meta=i.Meta(mid27, 1)),
    i.Invoke(
      args=[
        i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
        i.VDeref(code.intern_var(u"pixie.stdlib", u"-str"), meta=i.Meta(mid29, 4)),
        i.VDeref(code.intern_var(u"pixie.stdlib", u"String"), meta=i.Meta(mid30, 14)),
        i.Fn(args=[kw(u"this"),kw(u"sb")],name=kw(u"fn_354"),
          body=i.TailCall(
            args=[
              i.Lookup(kw(u"sb"), meta=i.Meta(mid31, 6)),
              i.Lookup(kw(u"this"), meta=i.Meta(mid31, 9)),
            ],
            meta=i.Meta(mid31, 5)),
        ),
      ],
      meta=nil),
    i.Invoke(
      args=[
        i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=i.Meta(mid32, 2)),
        i.VDeref(code.intern_var(u"pixie.stdlib", u"-eq"), meta=i.Meta(mid32, 9)),
        i.VDeref(code.intern_var(u"pixie.stdlib", u"Number"), meta=i.Meta(mid32, 13)),
        i.VDeref(code.intern_var(u"pixie.stdlib", u"-num-eq"), meta=i.Meta(mid32, 20)),
      ],
      meta=i.Meta(mid32, 1)),
    i.Invoke(args=[
# (def pixie.stdlib/+)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"+")),
      i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"multi-arity-fn")), i.Const(rt.wrap(u"+")),
              i.Const(rt.wrap(0)), i.Fn(args=[],name=kw(u"+"),
          body=i.Const(rt.wrap(0)),
        ),
        i.Const(rt.wrap(1)), i.Fn(args=[kw(u"x")],name=kw(u"+"),
          body=i.Lookup(kw(u"x"), meta=i.Meta(mid33, 8)),
        ),
        i.Const(rt.wrap(2)), i.Fn(args=[kw(u"x"),kw(u"y")],name=kw(u"+"),
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-add"), meta=i.Meta(mid34, 11)),
              i.Lookup(kw(u"x"), meta=i.Meta(mid34, 16)),
              i.Lookup(kw(u"y"), meta=i.Meta(mid34, 18)),
            ],
            meta=i.Meta(mid34, 10)),
        ),
                i.Const(rt.wrap(-1)), 
        i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"variadic-fn")), i.Const(rt.wrap(2)), 
        i.Fn(args=[kw(u"x"),kw(u"y"),kw(u"more")],name=kw(u"+"),
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-apply"), meta=i.Meta(mid35, 5)),
              i.Lookup(kw(u"+"), meta=i.Meta(mid35, 12)),
              i.Invoke(
                args=[
                  i.Lookup(kw(u"+"), meta=i.Meta(mid35, 15)),
                  i.Lookup(kw(u"x"), meta=i.Meta(mid35, 17)),
                  i.Lookup(kw(u"y"), meta=i.Meta(mid35, 19)),
                ],
                meta=i.Meta(mid35, 14)),
              i.Lookup(kw(u"more"), meta=i.Meta(mid35, 22)),
            ],
            meta=i.Meta(mid35, 4)),
        )])
      ])]),
    i.Invoke(args=[
# (def pixie.stdlib/-)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"-")),
      i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"multi-arity-fn")), i.Const(rt.wrap(u"-")),
              i.Const(rt.wrap(0)), i.Fn(args=[],name=kw(u"-"),
          body=i.Const(rt.wrap(0)),
        ),
        i.Const(rt.wrap(1)), i.Fn(args=[kw(u"x")],name=kw(u"-"),
          body=i.Lookup(kw(u"x"), meta=i.Meta(mid36, 8)),
        ),
        i.Const(rt.wrap(2)), i.Fn(args=[kw(u"x"),kw(u"y")],name=kw(u"-"),
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-sub"), meta=i.Meta(mid37, 11)),
              i.Lookup(kw(u"x"), meta=i.Meta(mid37, 16)),
              i.Lookup(kw(u"y"), meta=i.Meta(mid37, 18)),
            ],
            meta=i.Meta(mid37, 10)),
        ),
                i.Const(rt.wrap(-1)), 
        i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"variadic-fn")), i.Const(rt.wrap(2)), 
        i.Fn(args=[kw(u"x"),kw(u"y"),kw(u"more")],name=kw(u"-"),
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-apply"), meta=i.Meta(mid38, 5)),
              i.Lookup(kw(u"-"), meta=i.Meta(mid38, 12)),
              i.Invoke(
                args=[
                  i.Lookup(kw(u"-"), meta=i.Meta(mid38, 15)),
                  i.Lookup(kw(u"x"), meta=i.Meta(mid38, 17)),
                  i.Lookup(kw(u"y"), meta=i.Meta(mid38, 19)),
                ],
                meta=i.Meta(mid38, 14)),
              i.Lookup(kw(u"more"), meta=i.Meta(mid38, 22)),
            ],
            meta=i.Meta(mid38, 4)),
        )])
      ])]),
    i.Invoke(args=[
# (def pixie.stdlib/inc)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"inc")),
      i.Fn(args=[kw(u"x")],name=kw(u"inc"),
        body=i.TailCall(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"+"), meta=i.Meta(mid39, 9)),
            i.Lookup(kw(u"x"), meta=i.Meta(mid39, 11)),
            i.Const(rt.wrap(1)),
          ],
          meta=i.Meta(mid39, 8)),
      )]),
    i.Invoke(args=[
# (def pixie.stdlib/dec)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"dec")),
      i.Fn(args=[kw(u"x")],name=kw(u"dec"),
        body=i.TailCall(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-"), meta=i.Meta(mid40, 9)),
            i.Lookup(kw(u"x"), meta=i.Meta(mid40, 11)),
            i.Const(rt.wrap(1)),
          ],
          meta=i.Meta(mid40, 8)),
      )]),
    i.Invoke(args=[
# (def pixie.stdlib/<)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"<")),
      i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"multi-arity-fn")), i.Const(rt.wrap(u"<")),
              i.Const(rt.wrap(2)), i.Fn(args=[kw(u"x"),kw(u"y")],name=kw(u"<"),
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-lt"), meta=i.Meta(mid41, 11)),
              i.Lookup(kw(u"x"), meta=i.Meta(mid41, 15)),
              i.Lookup(kw(u"y"), meta=i.Meta(mid41, 17)),
            ],
            meta=i.Meta(mid41, 10)),
        ),
                i.Const(rt.wrap(-1)), 
        i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"variadic-fn")), i.Const(rt.wrap(2)), 
        i.Fn(args=[kw(u"x"),kw(u"y"),kw(u"more")],name=kw(u"<"),
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-apply"), meta=i.Meta(mid42, 5)),
              i.Lookup(kw(u"<"), meta=i.Meta(mid42, 12)),
              i.Invoke(
                args=[
                  i.Lookup(kw(u"<"), meta=i.Meta(mid42, 15)),
                  i.Lookup(kw(u"x"), meta=i.Meta(mid42, 17)),
                  i.Lookup(kw(u"y"), meta=i.Meta(mid42, 19)),
                ],
                meta=i.Meta(mid42, 14)),
              i.Lookup(kw(u"more"), meta=i.Meta(mid42, 22)),
            ],
            meta=i.Meta(mid42, 4)),
        )])
      ])]),
    i.Invoke(args=[
# (def pixie.stdlib/>)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u">")),
      i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"multi-arity-fn")), i.Const(rt.wrap(u">")),
              i.Const(rt.wrap(2)), i.Fn(args=[kw(u"x"),kw(u"y")],name=kw(u">"),
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-gt"), meta=i.Meta(mid43, 11)),
              i.Lookup(kw(u"x"), meta=i.Meta(mid43, 15)),
              i.Lookup(kw(u"y"), meta=i.Meta(mid43, 17)),
            ],
            meta=i.Meta(mid43, 10)),
        ),
                i.Const(rt.wrap(-1)), 
        i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"variadic-fn")), i.Const(rt.wrap(2)), 
        i.Fn(args=[kw(u"x"),kw(u"y"),kw(u"more")],name=kw(u">"),
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-apply"), meta=i.Meta(mid44, 5)),
              i.Lookup(kw(u">"), meta=i.Meta(mid44, 12)),
              i.Invoke(
                args=[
                  i.Lookup(kw(u">"), meta=i.Meta(mid44, 15)),
                  i.Lookup(kw(u"x"), meta=i.Meta(mid44, 17)),
                  i.Lookup(kw(u"y"), meta=i.Meta(mid44, 19)),
                ],
                meta=i.Meta(mid44, 14)),
              i.Lookup(kw(u"more"), meta=i.Meta(mid44, 22)),
            ],
            meta=i.Meta(mid44, 4)),
        )])
      ])]),
    i.Invoke(args=[
# (def pixie.stdlib/=)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"=")),
      i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"multi-arity-fn")), i.Const(rt.wrap(u"=")),
              i.Const(rt.wrap(1)), i.Fn(args=[kw(u"x")],name=kw(u"="),
          body=i.Const(nil),
        ),
        i.Const(rt.wrap(2)), i.Fn(args=[kw(u"x"),kw(u"y")],name=kw(u"="),
          body=i.If(
            test=i.Invoke(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"identical?"), meta=i.Meta(mid45, 15)),
                i.Lookup(kw(u"x"), meta=i.Meta(mid45, 26)),
                i.Lookup(kw(u"y"), meta=i.Meta(mid45, 28)),
              ],
              meta=i.Meta(mid45, 14)),
            then=i.Const(nil),
            els=i.TailCall(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"-eq"), meta=i.Meta(mid46, 13)),
                i.Lookup(kw(u"x"), meta=i.Meta(mid46, 17)),
                i.Lookup(kw(u"y"), meta=i.Meta(mid46, 19)),
              ],
              meta=i.Meta(mid46, 12)),
            meta=i.Meta(mid45, 10)),
        ),
                i.Const(rt.wrap(-1)), 
        i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"variadic-fn")), i.Const(rt.wrap(2)), 
        i.Fn(args=[kw(u"x"),kw(u"y"),kw(u"rest")],name=kw(u"="),
          body=i.If(
            test=i.Invoke(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"eq"), meta=i.Meta(mid47, 22)),
                i.Lookup(kw(u"x"), meta=i.Meta(mid47, 25)),
                i.Lookup(kw(u"y"), meta=i.Meta(mid47, 27)),
              ],
              meta=i.Meta(mid47, 21)),
            then=i.TailCall(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"apply"), meta=i.Meta(mid48, 20)),
                i.Lookup(kw(u"="), meta=i.Meta(mid48, 26)),
                i.Lookup(kw(u"y"), meta=i.Meta(mid48, 28)),
                i.Lookup(kw(u"rest"), meta=i.Meta(mid48, 30)),
              ],
              meta=i.Meta(mid48, 19)),
            els=i.Const(nil),
            meta=i.Meta(mid47, 17)),
        )])
      ])]),
    i.Invoke(args=[
# (def pixie.stdlib/conj)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"conj")),
      i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"multi-arity-fn")), i.Const(rt.wrap(u"conj")),
              i.Const(rt.wrap(0)), i.Fn(args=[],name=kw(u"conj"),
          body=i.Invoke(args=[
            i.Const(code.intern_var(u"pixie.stdlib", u"array")),            ]),
        ),
        i.Const(rt.wrap(1)), i.Fn(args=[kw(u"coll")],name=kw(u"conj"),
          body=i.Lookup(kw(u"coll"), meta=i.Meta(mid49, 11)),
        ),
        i.Const(rt.wrap(2)), i.Fn(args=[kw(u"coll"),kw(u"itm")],name=kw(u"conj"),
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-conj"), meta=i.Meta(mid50, 16)),
              i.Lookup(kw(u"coll"), meta=i.Meta(mid50, 22)),
              i.Lookup(kw(u"itm"), meta=i.Meta(mid50, 27)),
            ],
            meta=i.Meta(mid50, 15)),
        ),
                i.Const(rt.wrap(-1)), 
        i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"variadic-fn")), i.Const(rt.wrap(2)), 
        i.Fn(args=[kw(u"coll"),kw(u"item"),kw(u"more")],name=kw(u"conj"),
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-apply"), meta=i.Meta(mid51, 5)),
              i.Lookup(kw(u"conj"), meta=i.Meta(mid51, 12)),
              i.Invoke(
                args=[
                  i.Lookup(kw(u"conj"), meta=i.Meta(mid51, 18)),
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"x"), meta=i.Meta(mid51, 23)),
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"y"), meta=i.Meta(mid51, 25)),
                ],
                meta=i.Meta(mid51, 17)),
              i.Lookup(kw(u"more"), meta=i.Meta(mid51, 28)),
            ],
            meta=i.Meta(mid51, 4)),
        )])
      ])]),
    i.Invoke(args=[
# (def pixie.stdlib/count)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"count")),
      i.Fn(args=[kw(u"coll")],name=kw(u"count"),
        body=i.TailCall(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-count"), meta=i.Meta(mid52, 12)),
            i.Lookup(kw(u"coll"), meta=i.Meta(mid52, 19)),
          ],
          meta=i.Meta(mid52, 11)),
      )]),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/Cons)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"Cons")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"create-type"), meta=nil),
              i.Const(kw(u"Cons")),
              i.Invoke(args=[
                i.Const(code.intern_var(u"pixie.stdlib", u"array")),                i.Const(kw(u"first")),
                i.Const(kw(u"next")),
                i.Const(kw(u"meta")),
                ]),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/->Cons)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"->Cons")),
          i.Fn(args=[kw(u"first"),kw(u"next"),kw(u"meta")],name=kw(u"->Cons"),
            body=i.TailCall(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"new"), meta=nil),
                i.VDeref(code.intern_var(u"pixie.stdlib", u"Cons"), meta=i.Meta(mid53, 10)),
                i.Lookup(kw(u"first"), meta=nil),
                i.Lookup(kw(u"next"), meta=nil),
                i.Lookup(kw(u"meta"), meta=nil),
              ],
              meta=nil),
          )]),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-first"), meta=i.Meta(mid54, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Cons"), meta=i.Meta(mid53, 10)),
            i.Fn(args=[kw(u"this")],name=kw(u"-first_Cons"),
              body=i.TailCall(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                  i.Lookup(kw(u"this"), meta=i.Meta(mid54, 12)),
                  i.Const(kw(u"first")),
                ],
                meta=nil),
            ),
          ],
          meta=nil),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-next"), meta=i.Meta(mid55, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Cons"), meta=i.Meta(mid53, 10)),
            i.Fn(args=[kw(u"this")],name=kw(u"-next_Cons"),
              body=i.TailCall(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                  i.Lookup(kw(u"this"), meta=i.Meta(mid55, 11)),
                  i.Const(kw(u"next")),
                ],
                meta=nil),
            ),
          ],
          meta=nil),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-seq"), meta=i.Meta(mid56, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Cons"), meta=i.Meta(mid53, 10)),
            i.Fn(args=[kw(u"this")],name=kw(u"-seq_Cons"),
              body=i.Lookup(kw(u"this"), meta=i.Meta(mid56, 16)),
            ),
          ],
          meta=nil),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-meta"), meta=i.Meta(mid57, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Cons"), meta=i.Meta(mid53, 10)),
            i.Fn(args=[kw(u"this")],name=kw(u"-meta_Cons"),
              body=i.TailCall(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                  i.Lookup(kw(u"this"), meta=i.Meta(mid57, 11)),
                  i.Const(kw(u"meta")),
                ],
                meta=nil),
            ),
          ],
          meta=nil),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-with-meta"), meta=i.Meta(mid58, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Cons"), meta=i.Meta(mid53, 10)),
            i.Fn(args=[kw(u"this"),kw(u"new-meta")],name=kw(u"-with-meta_Cons"),
              body=i.TailCall(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"->Cons"), meta=i.Meta(mid59, 6)),
                  i.Invoke(
                    args=[
                      i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                      i.Lookup(kw(u"this"), meta=i.Meta(mid58, 16)),
                      i.Const(kw(u"first")),
                    ],
                    meta=nil),
                  i.Invoke(
                    args=[
                      i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                      i.Lookup(kw(u"this"), meta=i.Meta(mid58, 16)),
                      i.Const(kw(u"next")),
                    ],
                    meta=nil),
                  i.Lookup(kw(u"new-meta"), meta=i.Meta(mid59, 24)),
                ],
                meta=i.Meta(mid59, 5)),
            ),
          ],
          meta=nil),
      ],
    meta=i.Meta(mid53, 1)),
    i.Invoke(args=[
# (def pixie.stdlib/cons)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"cons")),
      i.Fn(args=[kw(u"head"),kw(u"tail")],name=kw(u"cons"),
        body=i.TailCall(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"->Cons"), meta=i.Meta(mid60, 4)),
            i.Lookup(kw(u"head"), meta=i.Meta(mid60, 11)),
            i.Invoke(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"seq"), meta=i.Meta(mid60, 17)),
                i.Lookup(kw(u"tail"), meta=i.Meta(mid60, 21)),
              ],
              meta=i.Meta(mid60, 16)),
            i.Const(nil),
          ],
          meta=i.Meta(mid60, 3)),
      )]),
    i.Invoke(args=[
# (def pixie.stdlib/string-builder)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"string-builder")),
      i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"multi-arity-fn")), i.Const(rt.wrap(u"string-builder")),
              i.Const(rt.wrap(0)), i.Fn(args=[],name=kw(u"string-builder"),
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-string-builder"), meta=i.Meta(mid61, 8)),
            ],
            meta=i.Meta(mid61, 7)),
        ),
        i.Const(rt.wrap(1)), i.Fn(args=[kw(u"sb")],name=kw(u"string-builder"),
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-str"), meta=i.Meta(mid62, 10)),
              i.Lookup(kw(u"sb"), meta=i.Meta(mid62, 15)),
            ],
            meta=i.Meta(mid62, 9)),
        ),
        i.Const(rt.wrap(2)), i.Fn(args=[kw(u"sb"),kw(u"x")],name=kw(u"string-builder"),
          body=i.If(
            test=i.Invoke(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"instance?"), meta=i.Meta(mid63, 9)),
                i.VDeref(code.intern_var(u"pixie.stdlib", u"String"), meta=i.Meta(mid63, 19)),
                i.Lookup(kw(u"x"), meta=i.Meta(mid63, 26)),
              ],
              meta=i.Meta(mid63, 8)),
            then=i.TailCall(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"-add-to-string-builder"), meta=i.Meta(mid64, 7)),
                i.Lookup(kw(u"x"), meta=i.Meta(mid64, 30)),
              ],
              meta=i.Meta(mid64, 6)),
            els=i.TailCall(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"-add-to-string-bulder"), meta=i.Meta(mid65, 7)),
                i.Invoke(
                  args=[
                    i.VDeref(code.intern_var(u"pixie.stdlib", u"-str"), meta=i.Meta(mid65, 30)),
                    i.Lookup(kw(u"x"), meta=i.Meta(mid65, 35)),
                  ],
                  meta=i.Meta(mid65, 29)),
              ],
              meta=i.Meta(mid65, 6)),
            meta=i.Meta(mid63, 4)),
        ),
              ])]),
    i.Invoke(args=[
# (def pixie.stdlib/str)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"str")),
      i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"variadic-fn")), i.Const(rt.wrap(0)), 
      i.Fn(args=[kw(u"args")],name=kw(u"str"),
        body=i.TailCall(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"transduce"), meta=i.Meta(mid66, 4)),
            i.Invoke(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"map"), meta=i.Meta(mid67, 5)),
                i.Lookup(kw(u"str"), meta=i.Meta(mid67, 9)),
              ],
              meta=i.Meta(mid67, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"string-builder"), meta=i.Meta(mid68, 4)),
            i.Lookup(kw(u"args"), meta=i.Meta(mid69, 4)),
          ],
          meta=i.Meta(mid66, 3)),
      )])]),
    i.Invoke(args=[
# (def pixie.stdlib/println)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"println")),
      i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"variadic-fn")), i.Const(rt.wrap(0)), 
      i.Fn(args=[kw(u"args")],name=kw(u"println"),closed_overs=[kw(u"add-fn"),kw(u"sb")],
        body=i.Let(names=[kw(u"sb"),kw(u"add-fn")],
        bindings=[
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-string-builder"), meta=i.Meta(mid70, 13)),
            ],
            meta=i.Meta(mid70, 12)),
          i.Fn(args=[kw(u"x")],name=kw(u"fn_410"),closed_overs=[kw(u"sb")],
            body=i.TailCall(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"-add-to-string-builder"), meta=i.Meta(mid71, 19)),
                i.Lookup(kw(u"sb"), meta=i.Meta(mid71, 42)),
                i.Lookup(kw(u"x"), meta=i.Meta(mid71, 45)),
              ],
              meta=i.Meta(mid71, 18)),
          ),
          ],
          body=i.Do(
            args=[
              i.Let(names=[kw(u"idx"),kw(u"sb")],
              bindings=[
                i.Const(rt.wrap(0)),
                i.Lookup(kw(u"sb"), meta=i.Meta(mid72, 15)),
                ],
                body=i.Invoke(
                  args=[
                    i.Fn(args=[kw(u"idx"),kw(u"sb")],name=kw(u"pixie.compiler/__loop__fn__"),closed_overs=[kw(u"args"),kw(u"add-fn")],
                      body=i.Let(names=[kw(u"idx"),kw(u"sb")],
                      bindings=[
                        i.Lookup(kw(u"idx"), meta=i.Meta(mid73, 12)),
                        i.Lookup(kw(u"sb"), meta=i.Meta(mid72, 12)),
                        ],
                        body=i.If(
                          test=i.Invoke(
                            args=[
                              i.VDeref(code.intern_var(u"pixie.stdlib", u"<"), meta=i.Meta(mid74, 12)),
                              i.Lookup(kw(u"idx"), meta=i.Meta(mid74, 14)),
                              i.Invoke(
                                args=[
                                  i.VDeref(code.intern_var(u"pixie.stdlib", u"count"), meta=i.Meta(mid74, 19)),
                                  i.Lookup(kw(u"args"), meta=i.Meta(mid74, 25)),
                                ],
                                meta=i.Meta(mid74, 18)),
                            ],
                            meta=i.Meta(mid74, 11)),
                          then=i.TailCall(
                            args=[
                              i.Lookup(kw(u"pixie.compiler/__loop__fn__"), meta=nil),
                              i.Invoke(
                                args=[
                                  i.VDeref(code.intern_var(u"pixie.stdlib", u"inc"), meta=i.Meta(mid75, 17)),
                                  i.Lookup(kw(u"idx"), meta=i.Meta(mid75, 21)),
                                ],
                                meta=i.Meta(mid75, 16)),
                              i.Do(
                                args=[
                                  i.Invoke(
                                    args=[
                                      i.VDeref(code.intern_var(u"pixie.stdlib", u"-str"), meta=i.Meta(mid76, 21)),
                                      i.Invoke(
                                        args=[
                                          i.VDeref(code.intern_var(u"pixie.stdlib", u"aget"), meta=i.Meta(mid76, 27)),
                                          i.Lookup(kw(u"args"), meta=i.Meta(mid76, 32)),
                                          i.Lookup(kw(u"idx"), meta=i.Meta(mid76, 37)),
                                        ],
                                        meta=i.Meta(mid76, 26)),
                                      i.Lookup(kw(u"add-fn"), meta=i.Meta(mid76, 42)),
                                    ],
                                    meta=i.Meta(mid76, 20)),
                                  i.Invoke(
                                    args=[
                                      i.Lookup(kw(u"add-fn"), meta=i.Meta(mid77, 21)),
                                      i.Const(rt.wrap(u" ")),
                                    ],
                                    meta=i.Meta(mid77, 20)),
                                  i.Lookup(kw(u"sb"), meta=i.Meta(mid78, 18)),
                                ],
                              meta=i.Meta(mid76, 16)),
                            ],
                            meta=nil),
                          els=i.TailCall(
                            args=[
                              i.VDeref(code.intern_var(u"pixie.stdlib", u"-blocking-println"), meta=i.Meta(mid79, 10)),
                              i.Invoke(
                                args=[
                                  i.VDeref(code.intern_var(u"pixie.stdlib", u"-finish-string-builder"), meta=i.Meta(mid79, 29)),
                                  i.Lookup(kw(u"sb"), meta=i.Meta(mid79, 52)),
                                ],
                                meta=i.Meta(mid79, 28)),
                            ],
                            meta=i.Meta(mid79, 9)),
                          meta=i.Meta(mid74, 7)),
                        meta=nil),
                    ),
                    i.Lookup(kw(u"idx"), meta=i.Meta(mid73, 12)),
                    i.Lookup(kw(u"sb"), meta=i.Meta(mid72, 12)),
                  ],
                  meta=nil),
                meta=i.Meta(mid73, 5)),
              i.Const(nil),
            ],
          meta=nil),
          meta=i.Meta(mid70, 3)),
      )])]),
    i.Invoke(args=[
# (def pixie.stdlib/instance?)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"instance?")),
      i.Fn(args=[kw(u"t"),kw(u"x")],name=kw(u"instance?"),
        body=i.If(
          test=i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-satisfies?"), meta=i.Meta(mid80, 8)),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"ISeqable"), meta=i.Meta(mid80, 20)),
              i.Lookup(kw(u"t"), meta=i.Meta(mid80, 29)),
            ],
            meta=i.Meta(mid80, 7)),
          then=i.Let(names=[kw(u"ts")],
          bindings=[
            i.Invoke(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"seq"), meta=i.Meta(mid81, 15)),
                i.Lookup(kw(u"t"), meta=i.Meta(mid81, 19)),
              ],
              meta=i.Meta(mid81, 14)),
            ],
            body=i.If(
              test=i.Invoke(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"not"), meta=i.Meta(mid82, 12)),
                  i.Lookup(kw(u"ts"), meta=i.Meta(mid82, 16)),
                ],
                meta=i.Meta(mid82, 11)),
              then=i.Const(nil),
              els=i.If(
                test=i.Invoke(
                  args=[
                    i.VDeref(code.intern_var(u"pixie.stdlib", u"-instance?"), meta=i.Meta(mid83, 16)),
                    i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"first"), meta=i.Meta(mid83, 28)),
                        i.Lookup(kw(u"ts"), meta=i.Meta(mid83, 34)),
                      ],
                      meta=i.Meta(mid83, 27)),
                    i.Lookup(kw(u"x"), meta=i.Meta(mid83, 38)),
                  ],
                  meta=i.Meta(mid83, 15)),
                then=i.Const(nil),
                els=i.TailCall(
                  args=[
                    i.Lookup(kw(u"instance?"), meta=i.Meta(mid84, 14)),
                    i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"rest"), meta=i.Meta(mid84, 25)),
                        i.Lookup(kw(u"ts"), meta=i.Meta(mid84, 30)),
                      ],
                      meta=i.Meta(mid84, 24)),
                    i.Lookup(kw(u"x"), meta=i.Meta(mid84, 34)),
                  ],
                  meta=i.Meta(mid84, 13)),
                meta=i.Meta(mid83, 11)),
              meta=i.Meta(mid82, 7)),
            meta=i.Meta(mid81, 5)),
          els=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-instance?"), meta=i.Meta(mid85, 6)),
              i.Lookup(kw(u"t"), meta=i.Meta(mid85, 17)),
              i.Lookup(kw(u"x"), meta=i.Meta(mid85, 19)),
            ],
            meta=i.Meta(mid85, 5)),
          meta=i.Meta(mid80, 3)),
      )]),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/Reduced)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"Reduced")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"create-type"), meta=nil),
              i.Const(kw(u"Reduced")),
              i.Invoke(args=[
                i.Const(code.intern_var(u"pixie.stdlib", u"array")),                i.Const(kw(u"x")),
                ]),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/->Reduced)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"->Reduced")),
          i.Fn(args=[kw(u"x")],name=kw(u"->Reduced"),
            body=i.TailCall(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"new"), meta=nil),
                i.VDeref(code.intern_var(u"pixie.stdlib", u"Reduced"), meta=i.Meta(mid86, 10)),
                i.Lookup(kw(u"x"), meta=nil),
              ],
              meta=nil),
          )]),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-deref"), meta=i.Meta(mid87, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Reduced"), meta=i.Meta(mid86, 10)),
            i.Fn(args=[kw(u"this")],name=kw(u"-deref_Reduced"),
              body=i.TailCall(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                  i.Lookup(kw(u"this"), meta=i.Meta(mid87, 12)),
                  i.Const(kw(u"x")),
                ],
                meta=nil),
            ),
          ],
          meta=nil),
      ],
    meta=i.Meta(mid86, 1)),
    i.Invoke(args=[
# (def pixie.stdlib/reduced)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"reduced")),
      i.Fn(args=[kw(u"x")],name=kw(u"reduced"),
        body=i.TailCall(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"->Reduced"), meta=i.Meta(mid88, 4)),
            i.Lookup(kw(u"x"), meta=i.Meta(mid88, 14)),
          ],
          meta=i.Meta(mid88, 3)),
      )]),
    i.Invoke(args=[
# (def pixie.stdlib/reduced?)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"reduced?")),
      i.Fn(args=[kw(u"x")],name=kw(u"reduced?"),
        body=i.TailCall(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"instance?"), meta=i.Meta(mid89, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Reduced"), meta=i.Meta(mid89, 14)),
            i.Lookup(kw(u"x"), meta=i.Meta(mid89, 22)),
          ],
          meta=i.Meta(mid89, 3)),
      )]),
    i.Invoke(args=[
# (def pixie.stdlib/satisfies?)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"satisfies?")),
      i.Fn(args=[kw(u"p"),kw(u"x")],name=kw(u"satisfies?"),
        body=i.If(
          test=i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-satisfies?"), meta=i.Meta(mid90, 8)),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"ISeqable"), meta=i.Meta(mid90, 20)),
              i.Lookup(kw(u"p"), meta=i.Meta(mid90, 29)),
            ],
            meta=i.Meta(mid90, 7)),
          then=i.Let(names=[kw(u"ps")],
          bindings=[
            i.Invoke(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"seq"), meta=i.Meta(mid91, 15)),
                i.Lookup(kw(u"p"), meta=i.Meta(mid91, 19)),
              ],
              meta=i.Meta(mid91, 14)),
            ],
            body=i.If(
              test=i.Invoke(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"not"), meta=i.Meta(mid92, 12)),
                  i.Lookup(kw(u"ps"), meta=i.Meta(mid92, 16)),
                ],
                meta=i.Meta(mid92, 11)),
              then=i.Const(nil),
              els=i.If(
                test=i.Invoke(
                  args=[
                    i.VDeref(code.intern_var(u"pixie.stdlib", u"not"), meta=i.Meta(mid93, 16)),
                    i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"-satisfies?"), meta=i.Meta(mid93, 21)),
                        i.Invoke(
                          args=[
                            i.VDeref(code.intern_var(u"pixie.stdlib", u"first"), meta=i.Meta(mid93, 34)),
                            i.Lookup(kw(u"ps"), meta=i.Meta(mid93, 40)),
                          ],
                          meta=i.Meta(mid93, 33)),
                        i.Lookup(kw(u"x"), meta=i.Meta(mid93, 44)),
                      ],
                      meta=i.Meta(mid93, 20)),
                  ],
                  meta=i.Meta(mid93, 15)),
                then=i.Const(nil),
                els=i.TailCall(
                  args=[
                    i.Lookup(kw(u"satisfies?"), meta=i.Meta(mid94, 14)),
                    i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"rest"), meta=i.Meta(mid94, 26)),
                        i.Lookup(kw(u"ps"), meta=i.Meta(mid94, 31)),
                      ],
                      meta=i.Meta(mid94, 25)),
                    i.Lookup(kw(u"x"), meta=i.Meta(mid94, 35)),
                  ],
                  meta=i.Meta(mid94, 13)),
                meta=i.Meta(mid93, 11)),
              meta=i.Meta(mid92, 7)),
            meta=i.Meta(mid91, 5)),
          els=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-satisfies?"), meta=i.Meta(mid95, 6)),
              i.Lookup(kw(u"p"), meta=i.Meta(mid95, 18)),
              i.Lookup(kw(u"x"), meta=i.Meta(mid95, 20)),
            ],
            meta=i.Meta(mid95, 5)),
          meta=i.Meta(mid90, 3)),
      )]),
    i.Invoke(args=[
# (def pixie.stdlib/transduce)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"transduce")),
      i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"multi-arity-fn")), i.Const(rt.wrap(u"transduce")),
              i.Const(rt.wrap(3)), i.Fn(args=[kw(u"xform"),kw(u"rf"),kw(u"coll")],name=kw(u"transduce"),
          body=i.Let(names=[kw(u"f"),kw(u"result")],
          bindings=[
            i.Invoke(
              args=[
                i.Lookup(kw(u"xform"), meta=i.Meta(mid96, 13)),
                i.Lookup(kw(u"rf"), meta=i.Meta(mid96, 19)),
              ],
              meta=i.Meta(mid96, 12)),
            i.Invoke(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"-reduce"), meta=i.Meta(mid97, 18)),
                i.Lookup(kw(u"coll"), meta=i.Meta(mid97, 26)),
                i.Lookup(kw(u"f"), meta=i.Meta(mid97, 31)),
                i.Invoke(
                  args=[
                    i.Lookup(kw(u"f"), meta=i.Meta(mid97, 34)),
                  ],
                  meta=i.Meta(mid97, 33)),
              ],
              meta=i.Meta(mid97, 17)),
            ],
            body=i.TailCall(
              args=[
                i.Lookup(kw(u"f"), meta=i.Meta(mid98, 7)),
                i.Lookup(kw(u"result"), meta=i.Meta(mid98, 9)),
              ],
              meta=i.Meta(mid98, 6)),
            meta=i.Meta(mid96, 4)),
        ),
        i.Const(rt.wrap(2)), i.Fn(args=[kw(u"f"),kw(u"coll")],name=kw(u"transduce"),
          body=i.Let(names=[kw(u"result")],
          bindings=[
            i.Invoke(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"-reduce"), meta=i.Meta(mid99, 18)),
                i.Lookup(kw(u"coll"), meta=i.Meta(mid99, 26)),
                i.Lookup(kw(u"f"), meta=i.Meta(mid99, 31)),
                i.Invoke(
                  args=[
                    i.Lookup(kw(u"f"), meta=i.Meta(mid99, 34)),
                  ],
                  meta=i.Meta(mid99, 33)),
              ],
              meta=i.Meta(mid99, 17)),
            ],
            body=i.TailCall(
              args=[
                i.Lookup(kw(u"f"), meta=i.Meta(mid100, 7)),
                i.Lookup(kw(u"result"), meta=i.Meta(mid100, 9)),
              ],
              meta=i.Meta(mid100, 6)),
            meta=i.Meta(mid99, 4)),
        ),
        i.Const(rt.wrap(4)), i.Fn(args=[kw(u"xform"),kw(u"rf"),kw(u"init"),kw(u"coll")],name=kw(u"transduce"),
          body=i.Let(names=[kw(u"f"),kw(u"result")],
          bindings=[
            i.Invoke(
              args=[
                i.Lookup(kw(u"xform"), meta=i.Meta(mid101, 13)),
                i.Lookup(kw(u"rf"), meta=i.Meta(mid101, 19)),
              ],
              meta=i.Meta(mid101, 12)),
            i.Invoke(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"-reduce"), meta=i.Meta(mid102, 18)),
                i.Lookup(kw(u"coll"), meta=i.Meta(mid102, 26)),
                i.Lookup(kw(u"f"), meta=i.Meta(mid102, 31)),
                i.Lookup(kw(u"init"), meta=i.Meta(mid102, 33)),
              ],
              meta=i.Meta(mid102, 17)),
            ],
            body=i.TailCall(
              args=[
                i.Lookup(kw(u"f"), meta=i.Meta(mid103, 7)),
                i.Lookup(kw(u"result"), meta=i.Meta(mid103, 9)),
              ],
              meta=i.Meta(mid103, 6)),
            meta=i.Meta(mid101, 4)),
        ),
              ])]),
    i.Invoke(args=[
# (def pixie.stdlib/reduce)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"reduce")),
      i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"multi-arity-fn")), i.Const(rt.wrap(u"reduce")),
              i.Const(rt.wrap(3)), i.Fn(args=[kw(u"rf"),kw(u"init"),kw(u"col")],name=kw(u"reduce"),
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-reduce"), meta=i.Meta(mid104, 5)),
              i.Lookup(kw(u"col"), meta=i.Meta(mid104, 13)),
              i.Lookup(kw(u"rf"), meta=i.Meta(mid104, 17)),
              i.Lookup(kw(u"init"), meta=i.Meta(mid104, 20)),
            ],
            meta=i.Meta(mid104, 4)),
        ),
        i.Const(rt.wrap(2)), i.Fn(args=[kw(u"rf"),kw(u"col")],name=kw(u"reduce"),
          body=i.TailCall(
            args=[
              i.Lookup(kw(u"reduce"), meta=i.Meta(mid105, 5)),
              i.Lookup(kw(u"rf"), meta=i.Meta(mid105, 12)),
              i.Invoke(
                args=[
                  i.Lookup(kw(u"rf"), meta=i.Meta(mid105, 16)),
                ],
                meta=i.Meta(mid105, 15)),
              i.Lookup(kw(u"col"), meta=i.Meta(mid105, 20)),
            ],
            meta=i.Meta(mid105, 4)),
        ),
              ])]),
    i.Invoke(args=[
# (def pixie.stdlib/into)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"into")),
      i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"multi-arity-fn")), i.Const(rt.wrap(u"into")),
              i.Const(rt.wrap(3)), i.Fn(args=[kw(u"to"),kw(u"xform"),kw(u"from")],name=kw(u"into"),
          body=i.If(
            test=i.Invoke(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"satisfies?"), meta=i.Meta(mid106, 9)),
                i.VDeref(code.intern_var(u"pixie.stdlib", u"IToTransient"), meta=i.Meta(mid106, 20)),
                i.Lookup(kw(u"to"), meta=i.Meta(mid106, 33)),
              ],
              meta=i.Meta(mid106, 8)),
            then=i.TailCall(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"transduce"), meta=i.Meta(mid107, 7)),
                i.Lookup(kw(u"xform"), meta=i.Meta(mid107, 17)),
                i.VDeref(code.intern_var(u"pixie.stdlib", u"conj!"), meta=i.Meta(mid107, 23)),
                i.Invoke(
                  args=[
                    i.VDeref(code.intern_var(u"pixie.stdlib", u"transient"), meta=i.Meta(mid107, 30)),
                    i.Lookup(kw(u"to"), meta=i.Meta(mid107, 40)),
                  ],
                  meta=i.Meta(mid107, 29)),
                i.Lookup(kw(u"from"), meta=i.Meta(mid107, 44)),
              ],
              meta=i.Meta(mid107, 6)),
            els=i.TailCall(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"transduce"), meta=i.Meta(mid108, 7)),
                i.Lookup(kw(u"xform"), meta=i.Meta(mid108, 17)),
                i.VDeref(code.intern_var(u"pixie.stdlib", u"conj"), meta=i.Meta(mid108, 23)),
                i.Lookup(kw(u"to"), meta=i.Meta(mid108, 28)),
                i.Lookup(kw(u"from"), meta=i.Meta(mid108, 31)),
              ],
              meta=i.Meta(mid108, 6)),
            meta=i.Meta(mid106, 4)),
        ),
        i.Const(rt.wrap(2)), i.Fn(args=[kw(u"to"),kw(u"from")],name=kw(u"into"),
          body=i.If(
            test=i.Invoke(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"satisfies?"), meta=i.Meta(mid109, 9)),
                i.VDeref(code.intern_var(u"pixie.stdlib", u"IToTransient"), meta=i.Meta(mid109, 20)),
                i.Lookup(kw(u"to"), meta=i.Meta(mid109, 33)),
              ],
              meta=i.Meta(mid109, 8)),
            then=i.TailCall(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"persistent!"), meta=i.Meta(mid110, 7)),
                i.Invoke(
                  args=[
                    i.VDeref(code.intern_var(u"pixie.stdlib", u"reduce"), meta=i.Meta(mid110, 20)),
                    i.VDeref(code.intern_var(u"pixie.stdlib", u"conj!"), meta=i.Meta(mid110, 27)),
                    i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"transient"), meta=i.Meta(mid110, 34)),
                        i.Lookup(kw(u"to"), meta=i.Meta(mid110, 44)),
                      ],
                      meta=i.Meta(mid110, 33)),
                    i.Lookup(kw(u"from"), meta=i.Meta(mid110, 48)),
                  ],
                  meta=i.Meta(mid110, 19)),
              ],
              meta=i.Meta(mid110, 6)),
            els=i.TailCall(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"reduce"), meta=i.Meta(mid111, 7)),
                i.VDeref(code.intern_var(u"pixie.stdlib", u"conj"), meta=i.Meta(mid111, 14)),
                i.Lookup(kw(u"to"), meta=i.Meta(mid111, 19)),
                i.Lookup(kw(u"from"), meta=i.Meta(mid111, 22)),
              ],
              meta=i.Meta(mid111, 6)),
            meta=i.Meta(mid109, 4)),
        ),
              ])]),
    i.Invoke(args=[
# (def pixie.stdlib/map)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"map")),
      i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"multi-arity-fn")), i.Const(rt.wrap(u"map")),
              i.Const(rt.wrap(1)), i.Fn(args=[kw(u"f")],name=kw(u"map"),
          body=i.Fn(args=[kw(u"xf")],name=kw(u"fn_447"),closed_overs=[kw(u"f")],
            body=i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"multi-arity-fn")), i.Const(rt.wrap(u"fn_451")),
                          i.Const(rt.wrap(0)), i.Fn(args=[],name=kw(u"fn_451"),closed_overs=[kw(u"xf")],
                body=i.TailCall(
                  args=[
                    i.Lookup(kw(u"xf"), meta=i.Meta(mid112, 13)),
                  ],
                  meta=i.Meta(mid112, 12)),
              ),
              i.Const(rt.wrap(1)), i.Fn(args=[kw(u"result")],name=kw(u"fn_451"),closed_overs=[kw(u"xf")],
                body=i.TailCall(
                  args=[
                    i.Lookup(kw(u"xf"), meta=i.Meta(mid113, 19)),
                    i.Lookup(kw(u"result"), meta=i.Meta(mid113, 22)),
                  ],
                  meta=i.Meta(mid113, 18)),
              ),
              i.Const(rt.wrap(2)), i.Fn(args=[kw(u"result"),kw(u"item")],name=kw(u"fn_451"),closed_overs=[kw(u"xf"),kw(u"f")],
                body=i.TailCall(
                  args=[
                    i.Lookup(kw(u"xf"), meta=i.Meta(mid114, 24)),
                    i.Lookup(kw(u"result"), meta=i.Meta(mid114, 27)),
                    i.Invoke(
                      args=[
                        i.Lookup(kw(u"f"), meta=i.Meta(mid114, 35)),
                        i.Lookup(kw(u"item"), meta=i.Meta(mid114, 37)),
                      ],
                      meta=i.Meta(mid114, 34)),
                  ],
                  meta=i.Meta(mid114, 23)),
              ),
                          ]),
          ),
        ),
        i.Const(rt.wrap(2)), i.Fn(args=[kw(u"f"),kw(u"coll")],name=kw(u"map"),closed_overs=[kw(u"map")],
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"lazy-seq*"), meta=i.Meta(mid115, 5)),
              i.Fn(args=[],name=kw(u"fn_452"),closed_overs=[kw(u"map"),kw(u"f"),kw(u"coll")],
                body=i.Let(names=[kw(u"s")],
                bindings=[
                  i.Invoke(
                    args=[
                      i.VDeref(code.intern_var(u"pixie.stdlib", u"seq"), meta=i.Meta(mid116, 16)),
                      i.Lookup(kw(u"coll"), meta=i.Meta(mid116, 20)),
                    ],
                    meta=i.Meta(mid116, 15)),
                  ],
                  body=i.If(
                    test=i.Lookup(kw(u"s"), meta=i.Meta(mid117, 13)),
                    then=i.TailCall(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"cons"), meta=i.Meta(mid118, 12)),
                        i.Invoke(
                          args=[
                            i.Lookup(kw(u"f"), meta=i.Meta(mid118, 18)),
                            i.Invoke(
                              args=[
                                i.VDeref(code.intern_var(u"pixie.stdlib", u"first"), meta=i.Meta(mid118, 21)),
                                i.Lookup(kw(u"s"), meta=i.Meta(mid118, 27)),
                              ],
                              meta=i.Meta(mid118, 20)),
                          ],
                          meta=i.Meta(mid118, 17)),
                        i.Invoke(
                          args=[
                            i.Lookup(kw(u"map"), meta=i.Meta(mid119, 18)),
                            i.Lookup(kw(u"f"), meta=i.Meta(mid119, 22)),
                            i.Invoke(
                              args=[
                                i.VDeref(code.intern_var(u"pixie.stdlib", u"rest"), meta=i.Meta(mid119, 25)),
                                i.Lookup(kw(u"s"), meta=i.Meta(mid119, 30)),
                              ],
                              meta=i.Meta(mid119, 24)),
                          ],
                          meta=i.Meta(mid119, 17)),
                      ],
                      meta=i.Meta(mid118, 11)),
                    els=i.Const(nil),
                    meta=i.Meta(mid117, 9)),
                  meta=i.Meta(mid116, 7)),
              ),
            ],
            meta=i.Meta(mid115, 4)),
        ),
                i.Const(rt.wrap(-1)), 
        i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"variadic-fn")), i.Const(rt.wrap(1)), 
        i.Fn(args=[kw(u"f"),kw(u"colls")],name=kw(u"map"),closed_overs=[kw(u"step"),kw(u"map")],
          body=i.Let(names=[kw(u"step")],
          bindings=[
            i.Fn(args=[kw(u"cs")],name=kw(u"step"),closed_overs=[kw(u"step"),kw(u"map")],
              body=i.TailCall(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"lazy-seq*"), meta=i.Meta(mid120, 18)),
                  i.Fn(args=[],name=kw(u"fn_454"),closed_overs=[kw(u"step"),kw(u"map"),kw(u"cs")],
                    body=i.Let(names=[kw(u"ss")],
                    bindings=[
                      i.Invoke(
                        args=[
                          i.Lookup(kw(u"map"), meta=i.Meta(mid121, 30)),
                          i.VDeref(code.intern_var(u"pixie.stdlib", u"seq"), meta=i.Meta(mid121, 34)),
                          i.Lookup(kw(u"cs"), meta=i.Meta(mid121, 38)),
                        ],
                        meta=i.Meta(mid121, 29)),
                      ],
                      body=i.If(
                        test=i.Invoke(
                          args=[
                            i.VDeref(code.intern_var(u"pixie.stdlib", u"every?"), meta=i.Meta(mid122, 27)),
                            i.VDeref(code.intern_var(u"pixie.stdlib", u"identity"), meta=i.Meta(mid122, 34)),
                            i.Lookup(kw(u"ss"), meta=i.Meta(mid122, 43)),
                          ],
                          meta=i.Meta(mid122, 26)),
                        then=i.TailCall(
                          args=[
                            i.VDeref(code.intern_var(u"pixie.stdlib", u"cons"), meta=i.Meta(mid123, 25)),
                            i.Invoke(
                              args=[
                                i.Lookup(kw(u"map"), meta=i.Meta(mid123, 31)),
                                i.VDeref(code.intern_var(u"pixie.stdlib", u"first"), meta=i.Meta(mid123, 35)),
                                i.Lookup(kw(u"ss"), meta=i.Meta(mid123, 41)),
                              ],
                              meta=i.Meta(mid123, 30)),
                            i.Invoke(
                              args=[
                                i.Lookup(kw(u"step"), meta=i.Meta(mid123, 46)),
                                i.Invoke(
                                  args=[
                                    i.Lookup(kw(u"map"), meta=i.Meta(mid123, 52)),
                                    i.VDeref(code.intern_var(u"pixie.stdlib", u"rest"), meta=i.Meta(mid123, 56)),
                                    i.Lookup(kw(u"ss"), meta=i.Meta(mid123, 61)),
                                  ],
                                  meta=i.Meta(mid123, 51)),
                              ],
                              meta=i.Meta(mid123, 45)),
                          ],
                          meta=i.Meta(mid123, 24)),
                        els=i.Const(nil),
                        meta=i.Meta(mid122, 22)),
                      meta=i.Meta(mid121, 20)),
                  ),
                ],
                meta=i.Meta(mid120, 17)),
            ),
            ],
            body=i.TailCall(
              args=[
                i.Lookup(kw(u"map"), meta=i.Meta(mid124, 7)),
                i.Fn(args=[kw(u"args")],name=kw(u"fn_456"),closed_overs=[kw(u"f")],
                  body=i.TailCall(
                    args=[
                      i.VDeref(code.intern_var(u"pixie.stdlib", u"apply"), meta=i.Meta(mid124, 23)),
                      i.Lookup(kw(u"f"), meta=i.Meta(mid124, 29)),
                      i.Lookup(kw(u"args"), meta=i.Meta(mid124, 31)),
                    ],
                    meta=i.Meta(mid124, 22)),
                ),
                i.Invoke(
                  args=[
                    i.Lookup(kw(u"step"), meta=i.Meta(mid124, 39)),
                    i.Lookup(kw(u"colls"), meta=i.Meta(mid124, 44)),
                  ],
                  meta=i.Meta(mid124, 38)),
              ],
              meta=i.Meta(mid124, 6)),
            meta=i.Meta(mid125, 4)),
        )])
      ])]),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/Range)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"Range")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"create-type"), meta=nil),
              i.Const(kw(u"Range")),
              i.Invoke(args=[
                i.Const(code.intern_var(u"pixie.stdlib", u"array")),                i.Const(kw(u"start")),
                i.Const(kw(u"stop")),
                i.Const(kw(u"step")),
                ]),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/->Range)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"->Range")),
          i.Fn(args=[kw(u"start"),kw(u"stop"),kw(u"step")],name=kw(u"->Range"),
            body=i.TailCall(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"new"), meta=nil),
                i.VDeref(code.intern_var(u"pixie.stdlib", u"Range"), meta=i.Meta(mid126, 10)),
                i.Lookup(kw(u"start"), meta=nil),
                i.Lookup(kw(u"stop"), meta=nil),
                i.Lookup(kw(u"step"), meta=nil),
              ],
              meta=nil),
          )]),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-reduce"), meta=i.Meta(mid127, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Range"), meta=i.Meta(mid126, 10)),
            i.Fn(args=[kw(u"self"),kw(u"f"),kw(u"init")],name=kw(u"-reduce_Range"),
              body=i.Let(names=[kw(u"i"),kw(u"acc")],
              bindings=[
                i.Invoke(
                  args=[
                    i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                    i.Lookup(kw(u"self"), meta=i.Meta(mid127, 13)),
                    i.Const(kw(u"start")),
                  ],
                  meta=nil),
                i.Lookup(kw(u"init"), meta=i.Meta(mid128, 16)),
                ],
                body=i.TailCall(
                  args=[
                    i.Fn(args=[kw(u"i"),kw(u"acc")],name=kw(u"pixie.compiler/__loop__fn__"),closed_overs=[kw(u"self"),kw(u"f")],
                      body=i.Let(names=[kw(u"i"),kw(u"acc")],
                      bindings=[
                        i.Lookup(kw(u"i"), meta=i.Meta(mid129, 12)),
                        i.Lookup(kw(u"acc"), meta=i.Meta(mid128, 12)),
                        ],
                        body=i.Do(
                          args=[
                            i.Invoke(
                              args=[
                                i.VDeref(code.intern_var(u"pixie.stdlib", u"println"), meta=i.Meta(mid130, 8)),
                                i.Lookup(kw(u"i"), meta=i.Meta(mid130, 16)),
                              ],
                              meta=i.Meta(mid130, 7)),
                            i.If(
                              test=i.Let(names=[kw(u"r#__gensym_321")],
                              bindings=[
                                i.If(
                                  test=i.Invoke(
                                    args=[
                                      i.VDeref(code.intern_var(u"pixie.stdlib", u">"), meta=i.Meta(mid131, 21)),
                                      i.Invoke(
                                        args=[
                                          i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                                          i.Lookup(kw(u"self"), meta=i.Meta(mid127, 13)),
                                          i.Const(kw(u"step")),
                                        ],
                                        meta=nil),
                                      i.Const(rt.wrap(0)),
                                    ],
                                    meta=i.Meta(mid131, 20)),
                                  then=i.Invoke(
                                    args=[
                                      i.VDeref(code.intern_var(u"pixie.stdlib", u"<"), meta=i.Meta(mid131, 32)),
                                      i.Lookup(kw(u"i"), meta=i.Meta(mid131, 34)),
                                      i.Invoke(
                                        args=[
                                          i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                                          i.Lookup(kw(u"self"), meta=i.Meta(mid127, 13)),
                                          i.Const(kw(u"stop")),
                                        ],
                                        meta=nil),
                                    ],
                                    meta=i.Meta(mid131, 31)),
                                  els=i.Const(nil),
                                  meta=i.Meta(mid131, 15)),
                                ],
                                body=i.If(
                                  test=i.Lookup(kw(u"r#__gensym_321"), meta=nil),
                                  then=i.Lookup(kw(u"r#__gensym_321"), meta=nil),
                                  els=i.Let(names=[kw(u"r#__gensym_320")],
                                  bindings=[
                                    i.If(
                                      test=i.Invoke(
                                        args=[
                                          i.VDeref(code.intern_var(u"pixie.stdlib", u"<"), meta=i.Meta(mid132, 21)),
                                          i.Invoke(
                                            args=[
                                              i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                                              i.Lookup(kw(u"self"), meta=i.Meta(mid127, 13)),
                                              i.Const(kw(u"step")),
                                            ],
                                            meta=nil),
                                          i.Const(rt.wrap(0)),
                                        ],
                                        meta=i.Meta(mid132, 20)),
                                      then=i.Invoke(
                                        args=[
                                          i.VDeref(code.intern_var(u"pixie.stdlib", u">"), meta=i.Meta(mid132, 32)),
                                          i.Lookup(kw(u"i"), meta=i.Meta(mid132, 34)),
                                          i.Invoke(
                                            args=[
                                              i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                                              i.Lookup(kw(u"self"), meta=i.Meta(mid127, 13)),
                                              i.Const(kw(u"stop")),
                                            ],
                                            meta=nil),
                                        ],
                                        meta=i.Meta(mid132, 31)),
                                      els=i.Const(nil),
                                      meta=i.Meta(mid132, 15)),
                                    ],
                                    body=i.If(
                                      test=i.Lookup(kw(u"r#__gensym_320"), meta=nil),
                                      then=i.Lookup(kw(u"r#__gensym_320"), meta=nil),
                                      els=i.Invoke(
                                        args=[
                                          i.VDeref(code.intern_var(u"pixie.stdlib", u"="), meta=i.Meta(mid133, 21)),
                                          i.Invoke(
                                            args=[
                                              i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                                              i.Lookup(kw(u"self"), meta=i.Meta(mid127, 13)),
                                              i.Const(kw(u"step")),
                                            ],
                                            meta=nil),
                                          i.Const(rt.wrap(0)),
                                        ],
                                        meta=i.Meta(mid133, 15)),
                                      meta=nil),
                                    meta=nil),
                                  meta=nil),
                                meta=i.Meta(mid131, 11)),
                              then=i.Let(names=[kw(u"acc")],
                              bindings=[
                                i.Invoke(
                                  args=[
                                    i.Lookup(kw(u"f"), meta=i.Meta(mid134, 20)),
                                    i.Lookup(kw(u"acc"), meta=i.Meta(mid134, 22)),
                                    i.Lookup(kw(u"i"), meta=i.Meta(mid134, 26)),
                                  ],
                                  meta=i.Meta(mid134, 19)),
                                ],
                                body=i.If(
                                  test=i.Invoke(
                                    args=[
                                      i.VDeref(code.intern_var(u"pixie.stdlib", u"reduced?"), meta=i.Meta(mid135, 16)),
                                      i.Lookup(kw(u"acc"), meta=i.Meta(mid135, 25)),
                                    ],
                                    meta=i.Meta(mid135, 15)),
                                  then=i.TailCall(
                                    args=[
                                      i.VDeref(code.intern_var(u"pixie.stdlib", u"-deref"), meta=nil),
                                      i.Lookup(kw(u"acc"), meta=i.Meta(mid136, 14)),
                                    ],
                                    meta=i.Meta(mid136, 13)),
                                  els=i.TailCall(
                                    args=[
                                      i.Lookup(kw(u"pixie.compiler/__loop__fn__"), meta=nil),
                                      i.Invoke(
                                        args=[
                                          i.VDeref(code.intern_var(u"pixie.stdlib", u"+"), meta=i.Meta(mid137, 21)),
                                          i.Lookup(kw(u"i"), meta=i.Meta(mid137, 23)),
                                          i.Invoke(
                                            args=[
                                              i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                                              i.Lookup(kw(u"self"), meta=i.Meta(mid127, 13)),
                                              i.Const(kw(u"step")),
                                            ],
                                            meta=nil),
                                        ],
                                        meta=i.Meta(mid137, 20)),
                                      i.Lookup(kw(u"acc"), meta=i.Meta(mid137, 31)),
                                    ],
                                    meta=nil),
                                  meta=i.Meta(mid135, 11)),
                                meta=i.Meta(mid134, 9)),
                              els=i.Lookup(kw(u"acc"), meta=i.Meta(mid138, 9)),
                              meta=i.Meta(mid131, 7)),
                          ],
                        meta=nil),
                        meta=nil),
                    ),
                    i.Lookup(kw(u"i"), meta=i.Meta(mid129, 12)),
                    i.Lookup(kw(u"acc"), meta=i.Meta(mid128, 12)),
                  ],
                  meta=nil),
                meta=i.Meta(mid129, 5)),
            ),
          ],
          meta=nil),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-count"), meta=i.Meta(mid139, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Range"), meta=i.Meta(mid126, 10)),
            i.Fn(args=[kw(u"self")],name=kw(u"-count_Range"),
              body=i.If(
                test=i.Let(names=[kw(u"r#__gensym_321")],
                bindings=[
                  i.If(
                    test=i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"<"), meta=i.Meta(mid140, 19)),
                        i.Invoke(
                          args=[
                            i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                            i.Lookup(kw(u"self"), meta=i.Meta(mid139, 12)),
                            i.Const(kw(u"start")),
                          ],
                          meta=nil),
                        i.Invoke(
                          args=[
                            i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                            i.Lookup(kw(u"self"), meta=i.Meta(mid139, 12)),
                            i.Const(kw(u"stop")),
                          ],
                          meta=nil),
                      ],
                      meta=i.Meta(mid140, 18)),
                    then=i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"<"), meta=i.Meta(mid140, 34)),
                        i.Invoke(
                          args=[
                            i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                            i.Lookup(kw(u"self"), meta=i.Meta(mid139, 12)),
                            i.Const(kw(u"step")),
                          ],
                          meta=nil),
                        i.Const(rt.wrap(0)),
                      ],
                      meta=i.Meta(mid140, 33)),
                    els=i.Const(nil),
                    meta=i.Meta(mid140, 13)),
                  ],
                  body=i.If(
                    test=i.Lookup(kw(u"r#__gensym_321"), meta=nil),
                    then=i.Lookup(kw(u"r#__gensym_321"), meta=nil),
                    els=i.Let(names=[kw(u"r#__gensym_320")],
                    bindings=[
                      i.If(
                        test=i.Invoke(
                          args=[
                            i.VDeref(code.intern_var(u"pixie.stdlib", u">"), meta=i.Meta(mid141, 19)),
                            i.Invoke(
                              args=[
                                i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                                i.Lookup(kw(u"self"), meta=i.Meta(mid139, 12)),
                                i.Const(kw(u"start")),
                              ],
                              meta=nil),
                            i.Invoke(
                              args=[
                                i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                                i.Lookup(kw(u"self"), meta=i.Meta(mid139, 12)),
                                i.Const(kw(u"stop")),
                              ],
                              meta=nil),
                          ],
                          meta=i.Meta(mid141, 18)),
                        then=i.Invoke(
                          args=[
                            i.VDeref(code.intern_var(u"pixie.stdlib", u">"), meta=i.Meta(mid141, 34)),
                            i.Invoke(
                              args=[
                                i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                                i.Lookup(kw(u"self"), meta=i.Meta(mid139, 12)),
                                i.Const(kw(u"step")),
                              ],
                              meta=nil),
                            i.Const(rt.wrap(0)),
                          ],
                          meta=i.Meta(mid141, 33)),
                        els=i.Const(nil),
                        meta=i.Meta(mid141, 13)),
                      ],
                      body=i.If(
                        test=i.Lookup(kw(u"r#__gensym_320"), meta=nil),
                        then=i.Lookup(kw(u"r#__gensym_320"), meta=nil),
                        els=i.Invoke(
                          args=[
                            i.VDeref(code.intern_var(u"pixie.stdlib", u"="), meta=i.Meta(mid142, 14)),
                            i.Invoke(
                              args=[
                                i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                                i.Lookup(kw(u"self"), meta=i.Meta(mid139, 12)),
                                i.Const(kw(u"step")),
                              ],
                              meta=nil),
                            i.Const(rt.wrap(0)),
                          ],
                          meta=i.Meta(mid142, 13)),
                        meta=nil),
                      meta=nil),
                    meta=nil),
                  meta=i.Meta(mid140, 9)),
                then=i.Const(rt.wrap(0)),
                els=i.TailCall(
                  args=[
                    i.VDeref(code.intern_var(u"pixie.stdlib", u"abs"), meta=i.Meta(mid143, 8)),
                    i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"quot"), meta=i.Meta(mid143, 13)),
                        i.Invoke(
                          args=[
                            i.VDeref(code.intern_var(u"pixie.stdlib", u"-"), meta=i.Meta(mid143, 19)),
                            i.Invoke(
                              args=[
                                i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                                i.Lookup(kw(u"self"), meta=i.Meta(mid139, 12)),
                                i.Const(kw(u"start")),
                              ],
                              meta=nil),
                            i.Invoke(
                              args=[
                                i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                                i.Lookup(kw(u"self"), meta=i.Meta(mid139, 12)),
                                i.Const(kw(u"stop")),
                              ],
                              meta=nil),
                          ],
                          meta=i.Meta(mid143, 18)),
                        i.Invoke(
                          args=[
                            i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                            i.Lookup(kw(u"self"), meta=i.Meta(mid139, 12)),
                            i.Const(kw(u"step")),
                          ],
                          meta=nil),
                      ],
                      meta=i.Meta(mid143, 12)),
                  ],
                  meta=i.Meta(mid143, 7)),
                meta=i.Meta(mid140, 5)),
            ),
          ],
          meta=nil),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-nth"), meta=i.Meta(mid144, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Range"), meta=i.Meta(mid126, 10)),
            i.Fn(args=[kw(u"self"),kw(u"idx")],name=kw(u"-nth_Range"),
              body=i.If(
                test=i.Let(names=[kw(u"r#__gensym_320")],
                bindings=[
                  i.Invoke(
                    args=[
                      i.VDeref(code.intern_var(u"pixie.stdlib", u"="), meta=i.Meta(mid145, 16)),
                      i.Invoke(
                        args=[
                          i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                          i.Lookup(kw(u"self"), meta=i.Meta(mid144, 10)),
                          i.Const(kw(u"start")),
                        ],
                        meta=nil),
                      i.Invoke(
                        args=[
                          i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                          i.Lookup(kw(u"self"), meta=i.Meta(mid144, 10)),
                          i.Const(kw(u"stop")),
                        ],
                        meta=nil),
                      i.Const(rt.wrap(0)),
                    ],
                    meta=i.Meta(mid145, 15)),
                  ],
                  body=i.If(
                    test=i.Lookup(kw(u"r#__gensym_320"), meta=nil),
                    then=i.Lookup(kw(u"r#__gensym_320"), meta=nil),
                    els=i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"neg?"), meta=i.Meta(mid145, 33)),
                        i.Lookup(kw(u"idx"), meta=i.Meta(mid145, 38)),
                      ],
                      meta=i.Meta(mid145, 32)),
                    meta=nil),
                  meta=i.Meta(mid145, 11)),
                then=i.TailCall(
                  args=[
                    i.VDeref(code.intern_var(u"pixie.stdlib", u"throw"), meta=i.Meta(mid146, 8)),
                    i.Invoke(args=[
                      i.Const(code.intern_var(u"pixie.stdlib", u"array")),                      i.Const(kw(u"pixie.stdlib/OutOfRangeException")),
                      i.Const(rt.wrap(u"Index out of Range")),
                      ]),
                  ],
                  meta=i.Meta(mid146, 7)),
                els=i.Const(nil),
                meta=i.Meta(mid145, 5)),
            ),
          ],
          meta=nil),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-nth-not-found"), meta=i.Meta(mid147, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Range"), meta=i.Meta(mid126, 10)),
            i.Fn(args=[kw(u"self"),kw(u"idx"),kw(u"not-found")],name=kw(u"-nth-not-found_Range"),
              body=i.Let(names=[kw(u"cmp"),kw(u"val")],
              bindings=[
                i.If(
                  test=i.Invoke(
                    args=[
                      i.VDeref(code.intern_var(u"pixie.stdlib", u"<"), meta=i.Meta(mid148, 20)),
                      i.Invoke(
                        args=[
                          i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                          i.Lookup(kw(u"self"), meta=i.Meta(mid147, 20)),
                          i.Const(kw(u"start")),
                        ],
                        meta=nil),
                      i.Invoke(
                        args=[
                          i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                          i.Lookup(kw(u"self"), meta=i.Meta(mid147, 20)),
                          i.Const(kw(u"stop")),
                        ],
                        meta=nil),
                    ],
                    meta=i.Meta(mid148, 19)),
                  then=i.VDeref(code.intern_var(u"pixie.stdlib", u"<"), meta=i.Meta(mid148, 34)),
                  els=i.VDeref(code.intern_var(u"pixie.stdlib", u">"), meta=i.Meta(mid148, 36)),
                  meta=i.Meta(mid148, 15)),
                i.Invoke(
                  args=[
                    i.VDeref(code.intern_var(u"pixie.stdlib", u"+"), meta=i.Meta(mid149, 16)),
                    i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                        i.Lookup(kw(u"self"), meta=i.Meta(mid147, 20)),
                        i.Const(kw(u"start")),
                      ],
                      meta=nil),
                    i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"*"), meta=i.Meta(mid149, 25)),
                        i.Lookup(kw(u"idx"), meta=i.Meta(mid149, 27)),
                        i.Invoke(
                          args=[
                            i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                            i.Lookup(kw(u"self"), meta=i.Meta(mid147, 20)),
                            i.Const(kw(u"step")),
                          ],
                          meta=nil),
                      ],
                      meta=i.Meta(mid149, 24)),
                  ],
                  meta=i.Meta(mid149, 15)),
                ],
                body=i.If(
                  test=i.Invoke(
                    args=[
                      i.Lookup(kw(u"cmp"), meta=i.Meta(mid150, 12)),
                      i.Lookup(kw(u"val"), meta=i.Meta(mid150, 16)),
                      i.Invoke(
                        args=[
                          i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                          i.Lookup(kw(u"self"), meta=i.Meta(mid147, 20)),
                          i.Const(kw(u"stop")),
                        ],
                        meta=nil),
                    ],
                    meta=i.Meta(mid150, 11)),
                  then=i.Lookup(kw(u"val"), meta=i.Meta(mid151, 9)),
                  els=i.Lookup(kw(u"not-found"), meta=i.Meta(mid152, 8)),
                  meta=i.Meta(mid150, 7)),
                meta=i.Meta(mid148, 5)),
            ),
          ],
          meta=nil),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-seq"), meta=i.Meta(mid153, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Range"), meta=i.Meta(mid126, 10)),
            i.Fn(args=[kw(u"self")],name=kw(u"-seq_Range"),
              body=i.If(
                test=i.Let(names=[kw(u"r#__gensym_320")],
                bindings=[
                  i.If(
                    test=i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u">"), meta=i.Meta(mid154, 21)),
                        i.Invoke(
                          args=[
                            i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                            i.Lookup(kw(u"self"), meta=i.Meta(mid153, 10)),
                            i.Const(kw(u"step")),
                          ],
                          meta=nil),
                        i.Const(rt.wrap(0)),
                      ],
                      meta=i.Meta(mid154, 20)),
                    then=i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"<"), meta=i.Meta(mid154, 32)),
                        i.Invoke(
                          args=[
                            i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                            i.Lookup(kw(u"self"), meta=i.Meta(mid153, 10)),
                            i.Const(kw(u"start")),
                          ],
                          meta=nil),
                        i.Invoke(
                          args=[
                            i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                            i.Lookup(kw(u"self"), meta=i.Meta(mid153, 10)),
                            i.Const(kw(u"stop")),
                          ],
                          meta=nil),
                      ],
                      meta=i.Meta(mid154, 31)),
                    els=i.Const(nil),
                    meta=i.Meta(mid154, 15)),
                  ],
                  body=i.If(
                    test=i.Lookup(kw(u"r#__gensym_320"), meta=nil),
                    then=i.Lookup(kw(u"r#__gensym_320"), meta=nil),
                    els=i.If(
                      test=i.Invoke(
                        args=[
                          i.VDeref(code.intern_var(u"pixie.stdlib", u"<"), meta=i.Meta(mid155, 21)),
                          i.Invoke(
                            args=[
                              i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                              i.Lookup(kw(u"self"), meta=i.Meta(mid153, 10)),
                              i.Const(kw(u"step")),
                            ],
                            meta=nil),
                          i.Const(rt.wrap(0)),
                        ],
                        meta=i.Meta(mid155, 20)),
                      then=i.Invoke(
                        args=[
                          i.VDeref(code.intern_var(u"pixie.stdlib", u">"), meta=i.Meta(mid155, 32)),
                          i.Invoke(
                            args=[
                              i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                              i.Lookup(kw(u"self"), meta=i.Meta(mid153, 10)),
                              i.Const(kw(u"start")),
                            ],
                            meta=nil),
                          i.Invoke(
                            args=[
                              i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                              i.Lookup(kw(u"self"), meta=i.Meta(mid153, 10)),
                              i.Const(kw(u"stop")),
                            ],
                            meta=nil),
                        ],
                        meta=i.Meta(mid155, 31)),
                      els=i.Const(nil),
                      meta=i.Meta(mid155, 15)),
                    meta=nil),
                  meta=i.Meta(mid154, 11)),
                then=i.TailCall(
                  args=[
                    i.VDeref(code.intern_var(u"pixie.stdlib", u"cons"), meta=i.Meta(mid156, 8)),
                    i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                        i.Lookup(kw(u"self"), meta=i.Meta(mid153, 10)),
                        i.Const(kw(u"start")),
                      ],
                      meta=nil),
                    i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"lazy-seq*"), meta=i.Meta(mid156, 20)),
                        i.Fn(args=[],name=kw(u"fn_475"),closed_overs=[kw(u"self")],
                          body=i.TailCall(
                            args=[
                              i.VDeref(code.intern_var(u"pixie.stdlib", u"range"), meta=i.Meta(mid156, 32)),
                              i.Invoke(
                                args=[
                                  i.VDeref(code.intern_var(u"pixie.stdlib", u"+"), meta=i.Meta(mid156, 39)),
                                  i.Invoke(
                                    args=[
                                      i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                                      i.Lookup(kw(u"self"), meta=i.Meta(mid153, 10)),
                                      i.Const(kw(u"start")),
                                    ],
                                    meta=nil),
                                  i.Invoke(
                                    args=[
                                      i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                                      i.Lookup(kw(u"self"), meta=i.Meta(mid153, 10)),
                                      i.Const(kw(u"step")),
                                    ],
                                    meta=nil),
                                ],
                                meta=i.Meta(mid156, 38)),
                              i.Invoke(
                                args=[
                                  i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                                  i.Lookup(kw(u"self"), meta=i.Meta(mid153, 10)),
                                  i.Const(kw(u"stop")),
                                ],
                                meta=nil),
                              i.Invoke(
                                args=[
                                  i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                                  i.Lookup(kw(u"self"), meta=i.Meta(mid153, 10)),
                                  i.Const(kw(u"step")),
                                ],
                                meta=nil),
                            ],
                            meta=i.Meta(mid156, 31)),
                        ),
                      ],
                      meta=i.Meta(mid156, 19)),
                  ],
                  meta=i.Meta(mid156, 7)),
                els=i.Const(nil),
                meta=i.Meta(mid154, 5)),
            ),
          ],
          meta=nil),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-str"), meta=i.Meta(mid157, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Range"), meta=i.Meta(mid126, 10)),
            i.Fn(args=[kw(u"this"),kw(u"sbf")],name=kw(u"-str_Range"),
              body=i.TailCall(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"-str"), meta=i.Meta(mid158, 6)),
                  i.Invoke(
                    args=[
                      i.VDeref(code.intern_var(u"pixie.stdlib", u"seq"), meta=i.Meta(mid158, 12)),
                      i.Lookup(kw(u"this"), meta=i.Meta(mid158, 16)),
                    ],
                    meta=i.Meta(mid158, 11)),
                  i.Lookup(kw(u"sbf"), meta=i.Meta(mid158, 22)),
                ],
                meta=i.Meta(mid158, 5)),
            ),
          ],
          meta=nil),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-repr"), meta=i.Meta(mid159, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Range"), meta=i.Meta(mid126, 10)),
            i.Fn(args=[kw(u"this"),kw(u"sbf")],name=kw(u"-repr_Range"),
              body=i.TailCall(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"-repr"), meta=i.Meta(mid160, 6)),
                  i.Invoke(
                    args=[
                      i.VDeref(code.intern_var(u"pixie.stdlib", u"seq"), meta=i.Meta(mid160, 13)),
                      i.Lookup(kw(u"this"), meta=i.Meta(mid160, 17)),
                    ],
                    meta=i.Meta(mid160, 12)),
                  i.Lookup(kw(u"sbf"), meta=i.Meta(mid160, 23)),
                ],
                meta=i.Meta(mid160, 5)),
            ),
          ],
          meta=nil),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-eq"), meta=i.Meta(mid161, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Range"), meta=i.Meta(mid126, 10)),
            i.Fn(args=[kw(u"this"),kw(u"sb")],name=kw(u"-eq_Range"),
              body=i.Const(nil),
            ),
          ],
          meta=nil),
      ],
    meta=i.Meta(mid126, 1)),
    i.Invoke(args=[
# (def pixie.stdlib/MAX-NUMBER)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"MAX-NUMBER")),
      i.Const(rt.wrap(4294967295))]),
    i.Invoke(args=[
# (def pixie.stdlib/range)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"range")),
      i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"multi-arity-fn")), i.Const(rt.wrap(u"range")),
              i.Const(rt.wrap(0)), i.Fn(args=[],name=kw(u"range"),
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"->Range"), meta=i.Meta(mid162, 8)),
              i.Const(rt.wrap(0)),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"MAX-NUMBER"), meta=i.Meta(mid162, 18)),
              i.Const(rt.wrap(1)),
            ],
            meta=i.Meta(mid162, 7)),
        ),
        i.Const(rt.wrap(1)), i.Fn(args=[kw(u"stop")],name=kw(u"range"),
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"->Range"), meta=i.Meta(mid163, 12)),
              i.Const(rt.wrap(0)),
              i.Lookup(kw(u"stop"), meta=i.Meta(mid163, 22)),
              i.Const(rt.wrap(1)),
            ],
            meta=i.Meta(mid163, 11)),
        ),
        i.Const(rt.wrap(3)), i.Fn(args=[kw(u"start"),kw(u"stop"),kw(u"step")],name=kw(u"range"),
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"->Range"), meta=i.Meta(mid164, 23)),
              i.Lookup(kw(u"start"), meta=i.Meta(mid164, 31)),
              i.Lookup(kw(u"stop"), meta=i.Meta(mid164, 37)),
              i.Lookup(kw(u"step"), meta=i.Meta(mid164, 42)),
            ],
            meta=i.Meta(mid164, 22)),
        ),
        i.Const(rt.wrap(2)), i.Fn(args=[kw(u"start"),kw(u"stop")],name=kw(u"range"),
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"->Range"), meta=i.Meta(mid165, 18)),
              i.Lookup(kw(u"start"), meta=i.Meta(mid165, 26)),
              i.Lookup(kw(u"stop"), meta=i.Meta(mid165, 32)),
              i.Const(rt.wrap(1)),
            ],
            meta=i.Meta(mid165, 17)),
        ),
              ])]),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/Node)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"Node")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"create-type"), meta=nil),
              i.Const(kw(u"Node")),
              i.Invoke(args=[
                i.Const(code.intern_var(u"pixie.stdlib", u"array")),                i.Const(kw(u"edit")),
                i.Const(kw(u"array")),
                ]),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/->Node)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"->Node")),
          i.Fn(args=[kw(u"edit"),kw(u"array")],name=kw(u"->Node"),
            body=i.TailCall(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"new"), meta=nil),
                i.VDeref(code.intern_var(u"pixie.stdlib", u"Node"), meta=i.Meta(mid166, 10)),
                i.Lookup(kw(u"edit"), meta=nil),
                i.Lookup(kw(u"array"), meta=nil),
              ],
              meta=nil),
          )]),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-get-field"), meta=i.Meta(mid167, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Node"), meta=i.Meta(mid166, 10)),
            i.Fn(args=[kw(u"this"),kw(u"name")],name=kw(u"-get-field_Node"),
              body=i.TailCall(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=i.Meta(mid168, 6)),
                  i.Lookup(kw(u"this"), meta=i.Meta(mid168, 16)),
                  i.Lookup(kw(u"name"), meta=i.Meta(mid168, 21)),
                ],
                meta=i.Meta(mid168, 5)),
            ),
          ],
          meta=nil),
      ],
    meta=i.Meta(mid166, 1)),
    i.Invoke(args=[
# (def pixie.stdlib/new-node)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"new-node")),
      i.Invoke([i.Const(code.intern_var(u"pixie.stdlib", u"multi-arity-fn")), i.Const(rt.wrap(u"new-node")),
              i.Const(rt.wrap(1)), i.Fn(args=[kw(u"edit")],name=kw(u"new-node"),
          body=i.TailCall(
            args=[
              i.Lookup(kw(u"new-node"), meta=i.Meta(mid169, 5)),
              i.Lookup(kw(u"edit"), meta=i.Meta(mid169, 14)),
              i.Invoke(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"array"), meta=i.Meta(mid169, 20)),
                  i.Const(rt.wrap(32)),
                ],
                meta=i.Meta(mid169, 19)),
            ],
            meta=i.Meta(mid169, 4)),
        ),
        i.Const(rt.wrap(2)), i.Fn(args=[kw(u"edit"),kw(u"array")],name=kw(u"new-node"),
          body=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"->Node"), meta=i.Meta(mid170, 5)),
              i.Lookup(kw(u"edit"), meta=i.Meta(mid170, 12)),
              i.Lookup(kw(u"array"), meta=i.Meta(mid170, 17)),
            ],
            meta=i.Meta(mid170, 4)),
        ),
              ])]),
    i.Invoke(args=[
# (def pixie.stdlib/EMPTY-NODE)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"EMPTY-NODE")),
      i.Invoke(
        args=[
          i.VDeref(code.intern_var(u"pixie.stdlib", u"new-node"), meta=i.Meta(mid171, 18)),
          i.Const(nil),
        ],
        meta=i.Meta(mid171, 17))]),
    i.Invoke(args=[
# (def pixie.stdlib/tailoff)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"tailoff")),
      i.Fn(args=[kw(u"this")],name=kw(u"tailoff"),
        body=i.Let(names=[kw(u"cnt")],
        bindings=[
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"-get-field"), meta=nil),
              i.Lookup(kw(u"this"), meta=i.Meta(mid172, 20)),
              i.Const(kw(u"cnt")),
            ],
            meta=i.Meta(mid172, 13)),
          ],
          body=i.If(
            test=i.Invoke(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"<"), meta=i.Meta(mid173, 10)),
                i.Lookup(kw(u"cnt"), meta=i.Meta(mid173, 12)),
                i.Const(rt.wrap(32)),
              ],
              meta=i.Meta(mid173, 9)),
            then=i.Const(rt.wrap(0)),
            els=i.TailCall(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"bit-shift-left"), meta=i.Meta(mid174, 8)),
                i.Invoke(
                  args=[
                    i.VDeref(code.intern_var(u"pixie.stdlib", u"bit-shift-right"), meta=i.Meta(mid174, 24)),
                    i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"dec"), meta=i.Meta(mid174, 41)),
                        i.Lookup(kw(u"cnt"), meta=i.Meta(mid174, 45)),
                      ],
                      meta=i.Meta(mid174, 40)),
                    i.Const(rt.wrap(5)),
                  ],
                  meta=i.Meta(mid174, 23)),
                i.Const(rt.wrap(5)),
              ],
              meta=i.Meta(mid174, 7)),
            meta=i.Meta(mid173, 5)),
          meta=i.Meta(mid172, 3)),
      )]),
    i.Invoke(args=[
# (def pixie.stdlib/array-for)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"array-for")),
      i.Fn(args=[kw(u"this"),kw(u"i"),kw(u"cnt"),kw(u"root"),kw(u"shift"),kw(u"tail")],name=kw(u"array-for"),
        body=i.If(
          test=i.If(
            test=i.Invoke(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"<="), meta=i.Meta(mid175, 17)),
                i.Const(rt.wrap(0)),
                i.Lookup(kw(u"i"), meta=i.Meta(mid175, 22)),
              ],
              meta=i.Meta(mid175, 16)),
            then=i.Invoke(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"<"), meta=i.Meta(mid175, 26)),
                i.Lookup(kw(u"i"), meta=i.Meta(mid175, 28)),
                i.Lookup(kw(u"cnt"), meta=i.Meta(mid175, 30)),
              ],
              meta=i.Meta(mid175, 25)),
            els=i.Const(nil),
            meta=i.Meta(mid175, 11)),
          then=i.If(
            test=i.Invoke(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u">="), meta=i.Meta(mid176, 14)),
                i.Lookup(kw(u"i"), meta=i.Meta(mid176, 17)),
                i.Invoke(
                  args=[
                    i.VDeref(code.intern_var(u"pixie.stdlib", u"tailoff"), meta=i.Meta(mid176, 20)),
                    i.Lookup(kw(u"this"), meta=i.Meta(mid176, 28)),
                  ],
                  meta=i.Meta(mid176, 19)),
              ],
              meta=i.Meta(mid176, 13)),
            then=i.Lookup(kw(u"tail"), meta=i.Meta(mid177, 11)),
            els=i.TailCall(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"-get-field"), meta=nil),
                i.Invoke(
                  args=[
                    i.Fn(args=[kw(u"node"),kw(u"level")],name=kw(u"look-deeper"),closed_overs=[kw(u"i")],
                      body=i.If(
                        test=i.Invoke(
                          args=[
                            i.VDeref(code.intern_var(u"pixie.stdlib", u">"), meta=i.Meta(mid178, 28)),
                            i.Lookup(kw(u"level"), meta=i.Meta(mid178, 30)),
                            i.Const(rt.wrap(0)),
                          ],
                          meta=i.Meta(mid178, 27)),
                        then=i.TailCall(
                          args=[
                            i.Lookup(kw(u"look-deeper"), meta=i.Meta(mid179, 26)),
                            i.Invoke(
                              args=[
                                i.VDeref(code.intern_var(u"pixie.stdlib", u"aget"), meta=i.Meta(mid179, 39)),
                                i.Invoke(
                                  args=[
                                    i.Const(kw(u"array")),
                                    i.Lookup(kw(u"node"), meta=i.Meta(mid179, 52)),
                                  ],
                                  meta=i.Meta(mid179, 44)),
                                i.Invoke(
                                  args=[
                                    i.VDeref(code.intern_var(u"pixie.stdlib", u"bit-and"), meta=i.Meta(mid180, 45)),
                                    i.Invoke(
                                      args=[
                                        i.VDeref(code.intern_var(u"pixie.stdlib", u"bit-shift-right"), meta=i.Meta(mid180, 54)),
                                        i.Lookup(kw(u"i"), meta=i.Meta(mid180, 70)),
                                        i.Lookup(kw(u"level"), meta=i.Meta(mid180, 72)),
                                      ],
                                      meta=i.Meta(mid180, 53)),
                                    i.Const(rt.wrap(31)),
                                  ],
                                  meta=i.Meta(mid180, 44)),
                              ],
                              meta=i.Meta(mid179, 38)),
                            i.Invoke(
                              args=[
                                i.VDeref(code.intern_var(u"pixie.stdlib", u"-"), meta=i.Meta(mid181, 39)),
                                i.Lookup(kw(u"level"), meta=i.Meta(mid181, 41)),
                                i.Const(rt.wrap(5)),
                              ],
                              meta=i.Meta(mid181, 38)),
                          ],
                          meta=i.Meta(mid179, 25)),
                        els=i.TailCall(
                          args=[
                            i.Const(kw(u"array")),
                            i.Lookup(kw(u"node"), meta=i.Meta(mid182, 33)),
                          ],
                          meta=i.Meta(mid182, 25)),
                        meta=i.Meta(mid178, 23)),
                    ),
                    i.Lookup(kw(u"root"), meta=i.Meta(mid183, 21)),
                    i.Lookup(kw(u"shift"), meta=i.Meta(mid184, 21)),
                  ],
                  meta=i.Meta(mid185, 20)),
                i.Const(kw(u"array")),
              ],
              meta=i.Meta(mid185, 11)),
            meta=i.Meta(mid176, 9)),
          els=i.Const(nil),
          meta=i.Meta(mid175, 7)),
      )]),
    i.Do(
      args=[
        i.Invoke(args=[
# (def pixie.stdlib/PersistentVector)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"PersistentVector")),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"create-type"), meta=nil),
              i.Const(kw(u"PersistentVector")),
              i.Invoke(args=[
                i.Const(code.intern_var(u"pixie.stdlib", u"array")),                i.Const(kw(u"cnt")),
                i.Const(kw(u"shift")),
                i.Const(kw(u"root")),
                i.Const(kw(u"tail")),
                i.Const(kw(u"meta")),
                ]),
            ],
            meta=nil)]),
        i.Invoke(args=[
# (def pixie.stdlib/->PersistentVector)
          i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
          i.Const(code.intern_var(u"pixie.stdlib",u"->PersistentVector")),
          i.Fn(args=[kw(u"cnt"),kw(u"shift"),kw(u"root"),kw(u"tail"),kw(u"meta")],name=kw(u"->PersistentVector"),
            body=i.TailCall(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"new"), meta=nil),
                i.VDeref(code.intern_var(u"pixie.stdlib", u"PersistentVector"), meta=i.Meta(mid186, 10)),
                i.Lookup(kw(u"cnt"), meta=nil),
                i.Lookup(kw(u"shift"), meta=nil),
                i.Lookup(kw(u"root"), meta=nil),
                i.Lookup(kw(u"tail"), meta=nil),
                i.Lookup(kw(u"meta"), meta=nil),
              ],
              meta=nil),
          )]),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-get-field"), meta=i.Meta(mid187, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"PersistentVector"), meta=i.Meta(mid186, 10)),
            i.Fn(args=[kw(u"this"),kw(u"name")],name=kw(u"-get-field_PersistentVector"),
              body=i.TailCall(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=i.Meta(mid188, 6)),
                  i.Lookup(kw(u"this"), meta=i.Meta(mid188, 16)),
                  i.Lookup(kw(u"name"), meta=i.Meta(mid188, 21)),
                ],
                meta=i.Meta(mid188, 5)),
            ),
          ],
          meta=nil),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-conj"), meta=i.Meta(mid189, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"PersistentVector"), meta=i.Meta(mid186, 10)),
            i.Fn(args=[kw(u"this"),kw(u"val")],name=kw(u"-conj_PersistentVector"),
              body=i.If(
                test=i.Invoke(
                  args=[
                    i.VDeref(code.intern_var(u"pixie.stdlib", u"<"), meta=i.Meta(mid190, 14)),
                    i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                        i.Lookup(kw(u"this"), meta=i.Meta(mid189, 11)),
                        i.Const(kw(u"cnt")),
                      ],
                      meta=nil),
                    i.Const(rt.wrap(4294967295)),
                  ],
                  meta=i.Meta(mid190, 13)),
                then=i.Const(nil),
                els=i.TailCall(
                  args=[
                    i.VDeref(code.intern_var(u"pixie.stdlib", u"throw"), meta=nil),
                    i.Invoke(args=[
                      i.Const(code.intern_var(u"pixie.stdlib", u"array")),                      i.Const(kw(u"pixie.stdlib/AssertionException")),
                      i.Invoke(
                        args=[
                          i.VDeref(code.intern_var(u"pixie.stdlib", u"str"), meta=nil),
                          i.Const(rt.wrap(u"Assert failed: ")),
                          i.Const(rt.wrap(u"Vector too large")),
                        ],
                        meta=nil),
                      ]),
                  ],
                  meta=nil),
                meta=i.Meta(mid190, 5)),
            ),
          ],
          meta=nil),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-count"), meta=i.Meta(mid191, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"PersistentVector"), meta=i.Meta(mid186, 10)),
            i.Fn(args=[kw(u"this")],name=kw(u"-count_PersistentVector"),
              body=i.TailCall(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"get-field"), meta=nil),
                  i.Lookup(kw(u"this"), meta=i.Meta(mid191, 12)),
                  i.Const(kw(u"cnt")),
                ],
                meta=nil),
            ),
          ],
          meta=nil),
      ],
    meta=i.Meta(mid186, 1)),
    i.Invoke(args=[
# (def pixie.stdlib/push-tail)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"push-tail")),
      i.Fn(args=[kw(u"this"),kw(u"level"),kw(u"parent"),kw(u"tail-node")],name=kw(u"push-tail"),
        body=i.Let(names=[kw(u"subidx"),kw(u"ret-array"),kw(u"node-to-insert")],
        bindings=[
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"bit-and"), meta=i.Meta(mid192, 17)),
              i.Invoke(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"bit-shift-right"), meta=i.Meta(mid192, 26)),
                  i.Invoke(
                    args=[
                      i.VDeref(code.intern_var(u"pixie.stdlib", u"dec"), meta=i.Meta(mid192, 43)),
                      i.Invoke(
                        args=[
                          i.VDeref(code.intern_var(u"pixie.stdlib", u"-get-field"), meta=nil),
                          i.Lookup(kw(u"this"), meta=i.Meta(mid192, 54)),
                          i.Const(kw(u"cnt")),
                        ],
                        meta=i.Meta(mid192, 47)),
                    ],
                    meta=i.Meta(mid192, 42)),
                  i.Lookup(kw(u"level"), meta=i.Meta(mid192, 61)),
                ],
                meta=i.Meta(mid192, 25)),
              i.Const(rt.wrap(31)),
            ],
            meta=i.Meta(mid192, 16)),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"aclone"), meta=i.Meta(mid193, 20)),
              i.Invoke(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"-get-field"), meta=nil),
                  i.Lookup(kw(u"parent"), meta=i.Meta(mid193, 36)),
                  i.Const(kw(u"array")),
                ],
                meta=i.Meta(mid193, 27)),
            ],
            meta=i.Meta(mid193, 19)),
          i.If(
            test=i.Invoke(
              args=[
                i.VDeref(code.intern_var(u"pixie.stdlib", u"="), meta=i.Meta(mid194, 29)),
                i.Lookup(kw(u"level"), meta=i.Meta(mid194, 31)),
                i.Const(rt.wrap(5)),
              ],
              meta=i.Meta(mid194, 28)),
            then=i.Lookup(kw(u"tail-node"), meta=i.Meta(mid195, 26)),
            els=i.Let(names=[kw(u"child")],
            bindings=[
              i.Invoke(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"aget"), meta=i.Meta(mid196, 39)),
                  i.Invoke(
                    args=[
                      i.VDeref(code.intern_var(u"pixie.stdlib", u"-get-field"), meta=nil),
                      i.Lookup(kw(u"parent"), meta=i.Meta(mid196, 53)),
                      i.Const(kw(u"array")),
                    ],
                    meta=i.Meta(mid196, 44)),
                  i.Lookup(kw(u"subidx"), meta=i.Meta(mid196, 61)),
                ],
                meta=i.Meta(mid196, 38)),
              ],
              body=i.If(
                test=i.Invoke(
                  args=[
                    i.VDeref(code.intern_var(u"pixie.stdlib", u"="), meta=i.Meta(mid197, 33)),
                    i.Lookup(kw(u"child"), meta=i.Meta(mid197, 35)),
                    i.Const(nil),
                  ],
                  meta=i.Meta(mid197, 32)),
                then=i.Invoke(
                  args=[
                    i.VDeref(code.intern_var(u"pixie.stdlib", u"new-path"), meta=i.Meta(mid198, 31)),
                    i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"-get-field"), meta=nil),
                        i.Invoke(
                          args=[
                            i.VDeref(code.intern_var(u"pixie.stdlib", u"-get-field"), meta=nil),
                            i.Lookup(kw(u"this"), meta=i.Meta(mid198, 56)),
                            i.Const(kw(u"root")),
                          ],
                          meta=i.Meta(mid198, 48)),
                        i.Const(kw(u"edit")),
                      ],
                      meta=i.Meta(mid198, 40)),
                    i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"-"), meta=i.Meta(mid199, 41)),
                        i.Lookup(kw(u"level"), meta=i.Meta(mid199, 43)),
                        i.Const(rt.wrap(5)),
                      ],
                      meta=i.Meta(mid199, 40)),
                    i.Lookup(kw(u"tail-node"), meta=i.Meta(mid200, 40)),
                  ],
                  meta=i.Meta(mid198, 30)),
                els=i.Invoke(
                  args=[
                    i.Lookup(kw(u"push-tail"), meta=i.Meta(mid201, 31)),
                    i.Lookup(kw(u"this"), meta=i.Meta(mid201, 41)),
                    i.Invoke(
                      args=[
                        i.VDeref(code.intern_var(u"pixie.stdlib", u"-"), meta=i.Meta(mid202, 42)),
                        i.Lookup(kw(u"level"), meta=i.Meta(mid202, 44)),
                        i.Const(rt.wrap(5)),
                      ],
                      meta=i.Meta(mid202, 41)),
                    i.Lookup(kw(u"child"), meta=i.Meta(mid203, 41)),
                    i.Lookup(kw(u"tail-node"), meta=i.Meta(mid204, 41)),
                  ],
                  meta=i.Meta(mid201, 30)),
                meta=i.Meta(mid197, 28)),
              meta=i.Meta(mid196, 26)),
            meta=i.Meta(mid194, 24)),
          ],
          body=i.Do(
            args=[
              i.Invoke(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"aset"), meta=i.Meta(mid205, 6)),
                  i.Lookup(kw(u"ret-array"), meta=i.Meta(mid205, 11)),
                  i.Lookup(kw(u"subidx"), meta=i.Meta(mid205, 21)),
                  i.Lookup(kw(u"node-to-insert"), meta=i.Meta(mid205, 28)),
                ],
                meta=i.Meta(mid205, 5)),
              i.TailCall(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"->Node"), meta=i.Meta(mid206, 6)),
                  i.Invoke(
                    args=[
                      i.VDeref(code.intern_var(u"pixie.stdlib", u"-get-field"), meta=nil),
                      i.Lookup(kw(u"parent"), meta=i.Meta(mid206, 21)),
                      i.Const(kw(u"edit")),
                    ],
                    meta=i.Meta(mid206, 13)),
                  i.Lookup(kw(u"node-to-insert"), meta=i.Meta(mid206, 29)),
                ],
                meta=i.Meta(mid206, 5)),
            ],
          meta=nil),
          meta=i.Meta(mid192, 3)),
      )]),
    i.Invoke(args=[
# (def pixie.stdlib/new-path)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"new-path")),
      i.Fn(args=[kw(u"edit"),kw(u"level"),kw(u"node")],name=kw(u"new-path"),
        body=i.If(
          test=i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"="), meta=i.Meta(mid207, 8)),
              i.Lookup(kw(u"level"), meta=i.Meta(mid207, 10)),
              i.Const(rt.wrap(0)),
            ],
            meta=i.Meta(mid207, 7)),
          then=i.Lookup(kw(u"node"), meta=i.Meta(mid208, 5)),
          els=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"->Node"), meta=i.Meta(mid209, 6)),
              i.Lookup(kw(u"edit"), meta=i.Meta(mid209, 13)),
              i.Invoke(
                args=[
                  i.Lookup(kw(u"new-path"), meta=i.Meta(mid210, 14)),
                  i.Lookup(kw(u"edit"), meta=i.Meta(mid210, 23)),
                  i.Invoke(
                    args=[
                      i.VDeref(code.intern_var(u"pixie.stdlib", u"-"), meta=i.Meta(mid210, 29)),
                      i.Lookup(kw(u"level"), meta=i.Meta(mid210, 31)),
                      i.Const(rt.wrap(5)),
                    ],
                    meta=i.Meta(mid210, 28)),
                  i.Lookup(kw(u"node"), meta=i.Meta(mid210, 40)),
                ],
                meta=i.Meta(mid210, 13)),
            ],
            meta=i.Meta(mid209, 5)),
          meta=i.Meta(mid207, 3)),
      )]),
    i.Invoke(args=[
# (def pixie.stdlib/EMPTY)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"EMPTY")),
      i.Invoke(
        args=[
          i.VDeref(code.intern_var(u"pixie.stdlib", u"->PersistentVector"), meta=i.Meta(mid211, 13)),
          i.Const(rt.wrap(0)),
          i.Const(rt.wrap(5)),
          i.VDeref(code.intern_var(u"pixie.stdlib", u"EMPTY-NODE"), meta=i.Meta(mid211, 36)),
          i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"array"), meta=i.Meta(mid211, 48)),
              i.Const(rt.wrap(0)),
            ],
            meta=i.Meta(mid211, 47)),
          i.Const(nil),
        ],
        meta=i.Meta(mid211, 12))]),
    i.Invoke(args=[
# (def pixie.stdlib/vector-from-array)
      i.Const(code.intern_var(u"pixie.stdlib", u"set-var-root!")),
      i.Const(code.intern_var(u"pixie.stdlib",u"vector-from-array")),
      i.Fn(args=[kw(u"arr")],name=kw(u"vector-from-array"),
        body=i.If(
          test=i.Invoke(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"<"), meta=i.Meta(mid212, 8)),
              i.Invoke(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"count"), meta=i.Meta(mid212, 11)),
                  i.Lookup(kw(u"arr"), meta=i.Meta(mid212, 17)),
                ],
                meta=i.Meta(mid212, 10)),
              i.Const(rt.wrap(32)),
            ],
            meta=i.Meta(mid212, 7)),
          then=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"->PersistentVector"), meta=i.Meta(mid213, 6)),
              i.Invoke(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"count"), meta=i.Meta(mid213, 26)),
                  i.Lookup(kw(u"arr"), meta=i.Meta(mid213, 32)),
                ],
                meta=i.Meta(mid213, 25)),
              i.Const(rt.wrap(5)),
              i.VDeref(code.intern_var(u"pixie.stdlib", u"EMPTY-NODE"), meta=i.Meta(mid213, 39)),
              i.Lookup(kw(u"arr"), meta=i.Meta(mid213, 50)),
              i.Const(nil),
            ],
            meta=i.Meta(mid213, 5)),
          els=i.TailCall(
            args=[
              i.VDeref(code.intern_var(u"pixie.stdlib", u"into"), meta=i.Meta(mid214, 6)),
              i.Invoke(args=[
                i.Const(code.intern_var(u"pixie.stdlib", u"array")),                ]),
              i.Lookup(kw(u"arr"), meta=i.Meta(mid214, 14)),
            ],
            meta=i.Meta(mid214, 5)),
          meta=i.Meta(mid212, 3)),
      )]),
    i.Do(
      args=[
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-reduce"), meta=i.Meta(mid215, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Array"), meta=i.Meta(mid216, 14)),
            i.Fn(args=[kw(u"this"),kw(u"f"),kw(u"init")],name=kw(u"fn_528"),
              body=i.Let(names=[kw(u"idx"),kw(u"acc")],
              bindings=[
                i.Const(rt.wrap(0)),
                i.Lookup(kw(u"init"), meta=i.Meta(mid217, 16)),
                ],
                body=i.TailCall(
                  args=[
                    i.Fn(args=[kw(u"idx"),kw(u"acc")],name=kw(u"pixie.compiler/__loop__fn__"),closed_overs=[kw(u"this"),kw(u"f")],
                      body=i.Let(names=[kw(u"idx"),kw(u"acc")],
                      bindings=[
                        i.Lookup(kw(u"idx"), meta=i.Meta(mid218, 12)),
                        i.Lookup(kw(u"acc"), meta=i.Meta(mid217, 12)),
                        ],
                        body=i.If(
                          test=i.Invoke(
                            args=[
                              i.VDeref(code.intern_var(u"pixie.stdlib", u"reduced?"), meta=i.Meta(mid219, 12)),
                              i.Lookup(kw(u"acc"), meta=i.Meta(mid219, 21)),
                            ],
                            meta=i.Meta(mid219, 11)),
                          then=i.TailCall(
                            args=[
                              i.VDeref(code.intern_var(u"pixie.stdlib", u"-deref"), meta=nil),
                              i.Lookup(kw(u"acc"), meta=i.Meta(mid220, 10)),
                            ],
                            meta=i.Meta(mid220, 9)),
                          els=i.If(
                            test=i.Invoke(
                              args=[
                                i.VDeref(code.intern_var(u"pixie.stdlib", u"<"), meta=i.Meta(mid221, 14)),
                                i.Lookup(kw(u"idx"), meta=i.Meta(mid221, 16)),
                                i.Invoke(
                                  args=[
                                    i.VDeref(code.intern_var(u"pixie.stdlib", u"count"), meta=i.Meta(mid221, 21)),
                                    i.Lookup(kw(u"this"), meta=i.Meta(mid221, 27)),
                                  ],
                                  meta=i.Meta(mid221, 20)),
                              ],
                              meta=i.Meta(mid221, 13)),
                            then=i.TailCall(
                              args=[
                                i.Lookup(kw(u"pixie.compiler/__loop__fn__"), meta=nil),
                                i.Invoke(
                                  args=[
                                    i.VDeref(code.intern_var(u"pixie.stdlib", u"inc"), meta=i.Meta(mid222, 19)),
                                    i.Lookup(kw(u"idx"), meta=i.Meta(mid222, 23)),
                                  ],
                                  meta=i.Meta(mid222, 18)),
                                i.Invoke(
                                  args=[
                                    i.Lookup(kw(u"f"), meta=i.Meta(mid223, 19)),
                                    i.Lookup(kw(u"acc"), meta=i.Meta(mid223, 21)),
                                    i.Invoke(
                                      args=[
                                        i.VDeref(code.intern_var(u"pixie.stdlib", u"aget"), meta=i.Meta(mid223, 26)),
                                        i.Lookup(kw(u"this"), meta=i.Meta(mid223, 31)),
                                        i.Lookup(kw(u"idx"), meta=i.Meta(mid223, 36)),
                                      ],
                                      meta=i.Meta(mid223, 25)),
                                  ],
                                  meta=i.Meta(mid223, 18)),
                              ],
                              meta=nil),
                            els=i.Lookup(kw(u"acc"), meta=i.Meta(mid224, 11)),
                            meta=i.Meta(mid221, 9)),
                          meta=i.Meta(mid219, 7)),
                        meta=nil),
                    ),
                    i.Lookup(kw(u"idx"), meta=i.Meta(mid218, 12)),
                    i.Lookup(kw(u"acc"), meta=i.Meta(mid217, 12)),
                  ],
                  meta=nil),
                meta=i.Meta(mid218, 5)),
            ),
          ],
          meta=nil),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-count"), meta=i.Meta(mid225, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Array"), meta=i.Meta(mid216, 14)),
            i.Fn(args=[kw(u"arr")],name=kw(u"fn_532"),
              body=i.TailCall(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"-get-field"), meta=nil),
                  i.Lookup(kw(u"arr"), meta=i.Meta(mid226, 21)),
                  i.Const(kw(u"count")),
                ],
                meta=i.Meta(mid226, 12)),
            ),
          ],
          meta=nil),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"extend"), meta=nil),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"-conj"), meta=i.Meta(mid227, 4)),
            i.VDeref(code.intern_var(u"pixie.stdlib", u"Array"), meta=i.Meta(mid216, 14)),
            i.Fn(args=[kw(u"arr"),kw(u"itm")],name=kw(u"fn_524"),
              body=i.TailCall(
                args=[
                  i.VDeref(code.intern_var(u"pixie.stdlib", u"conj"), meta=i.Meta(mid228, 12)),
                  i.Invoke(
                    args=[
                      i.VDeref(code.intern_var(u"pixie.stdlib", u"vector-from-array"), meta=i.Meta(mid228, 18)),
                      i.Lookup(kw(u"arr"), meta=i.Meta(mid228, 36)),
                    ],
                    meta=i.Meta(mid228, 17)),
                  i.Lookup(kw(u"itm"), meta=i.Meta(mid228, 41)),
                ],
                meta=i.Meta(mid228, 11)),
            ),
          ],
          meta=nil),
      ],
    meta=i.Meta(mid216, 1)),
    i.Invoke(
      args=[
        i.VDeref(code.intern_var(u"pixie.stdlib", u"println"), meta=i.Meta(mid229, 2)),
        i.Const(rt.wrap(42)),
      ],
      meta=i.Meta(mid229, 1)),
    i.TailCall(
      args=[
        i.VDeref(code.intern_var(u"pixie.stdlib", u"into"), meta=i.Meta(mid230, 2)),
        i.Invoke(args=[
          i.Const(code.intern_var(u"pixie.stdlib", u"array")),          ]),
        i.Invoke(
          args=[
            i.VDeref(code.intern_var(u"pixie.stdlib", u"range"), meta=i.Meta(mid230, 11)),
            i.Const(rt.wrap(1000)),
          ],
          meta=i.Meta(mid230, 10)),
      ],
      meta=i.Meta(mid230, 1)),
  ],
meta=i.Meta(mid231, 1))